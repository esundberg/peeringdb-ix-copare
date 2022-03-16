from peeringdb import PeeringDB
import config as cfg

asn = input('Lookup ASN: ')
data = []

ixlist = {}
asn_data = {}

pdb = PeeringDB(
    server = cfg.peeringdb["server"],
    username = cfg.peeringdb["username"],
    password = cfg.peeringdb["password"])

# print "Get the Network Info
network = pdb.get_net(asn=asn)
if not network:
    print(f'No Results')
if "data" in network:
    if len(network["data"]) == 1:
        network = network["data"][0]
    else:
        print(f'We received more that one network expecting one network')
        exit()

else:
    print(f'Network Error nothing returned')
    exit()

#print(network)
print(f'Id: {network["id"]}')
print(f'OrgId: {network["org_id"]}')
print(f'Network: {network["name"]}')
print(f'ASN: {network["asn"]}')
print(f'IX Count: {network["ix_count"]}')
print(f'Facility Count: {network["fac_count"]}')

# Get a list of Facilities for our network
facilities = pdb.get_netfac(net_id=network["id"])
print(f'\n\nFacilities ({len(facilities["data"])})')
for fac in facilities["data"]:
    fac_name = f'{fac["fac_id"]}:{fac["name"]}'
    print(f'{fac_name:50.50} | {fac["city"]:25.25}')

ixlist = pdb.get_netixlan(asn=asn)
print(f'\n\nInternet Exchanges ({len(ixlist["data"])})')
for ix in ixlist["data"]:
    print(f"{ix['name']:50.50} | {str(ix['asn']):8.8} | {str(ix['speed']):8.8} | {ix['ipaddr4']:16.16} | {ix['ipaddr6']:36.36} | {ix['is_rs_peer']}")
