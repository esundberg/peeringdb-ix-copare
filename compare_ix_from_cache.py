import json


def load_file(filename):
    """
    Loads a file from JSON.
    :param filename:
    :return: dictionary
    """
    with open(filename) as fp:
        return json.load(fp)


def net_lookup(asn, cache):
    """
    Look Net by ASN from Cache
    :param asn:
    :param cache:
    :return:
    """
    for net in cache:
        if net["asn"] == asn:
            return net


def ix_lookup(ix_id, cache):
    """
    Lookup the IX info from the IX ID
    :param ix_id:
    :param cache:
    :return:
    """
    for ix in cache:
        if ix["id"] == ix_id:
            return ix


def compare_by_ix_id(ix_compare_list=[]):
    # Load the Cache json files
    net_cache = load_file('net.json')
    ix_cache = load_file('ix.json')
    # ixlan_cache = load_file('ixlan.json')
    # netfac_cache = load_file('netfac.json')
    netixlan_cache = load_file('netixlan.json')

    netixlan_filter_cache = []
    as_list = []

    for netixlan in netixlan_cache:
        if any(ix_id_check == netixlan["ix_id"] for ix_id_check in ix_compare_list):
            # Append as
            asn = netixlan['asn']
            if asn not in as_list:
                as_list.append(asn)

            # Build the netixlan filter cache
            netixlan_filter_cache.append(netixlan)

    print(f'ASNs: {len(as_list)}')
    print(f'Filtered netixlan: {len(netixlan_filter_cache)}')
    as_list.sort()

    # Header
    print(f"{'ASN':<10} | {'Name':<50} |", end='')
    for ix_id_compare in ix_compare_list:
        ix_info = ix_lookup(ix_id_compare, ix_cache)
        print(f' {ix_info["name"]:20.20} |', end='')
    print('')

    # Print each asn
    for asn in as_list:
        net_info = net_lookup(asn, net_cache)
        result = {}
        for ix_id in ix_compare_list:
            result[ix_id] = ''

        for ix_id in netixlan_filter_cache:
            for netixlan in netixlan_filter_cache:
                if netixlan['ix_id'] == ix_id["ix_id"] and netixlan['asn'] == asn:
                    result.update({ix_id["ix_id"]: True})

        print(f'{asn:10} | {net_info["name"]:50.50} |', end='')
        for ix_id_compare in ix_compare_list:
            print(f' {result[ix_id_compare]!s:^20} |', end='')
        print('')


if __name__ == '__main__':
    print(f'\n\nAtlanta')
    compare_by_ix_id([22, 9, 1668, 627])

    print(f'\n\nChicago')
    compare_by_ix_id([2, 239, 944, 3378, 2551])

    print(f'\n\nDallas')
    compare_by_ix_id([3, 1249, 1180, 322])

    print(f'\n\nDenver')
    compare_by_ix_id([254, 1207])

    print(f'\n\nLos Angeles')
    compare_by_ix_id([142, 11, 4, 1175, 23])

    print('\n\nNew York Metro')
    compare_by_ix_id([325, 804, 14])

    print('\n\nSeattle')
    compare_by_ix_id([13, 1174, 82, 11])
