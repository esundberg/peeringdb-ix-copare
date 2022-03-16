from peeringdb import PeeringDB
import config as cfg
import json
from pprint import pprint



pdb = PeeringDB(
    server = cfg.peeringdb["server"],
    username = cfg.peeringdb["username"],
    password = cfg.peeringdb["password"])
print(f'What do you want to cache?')
cache_ix = input("ix: ")
cache_net = input("nets: ")
cache_netfac = input("netfac: ")
cache_netixlan = input("netixlan: ")
cache_ixlan = input("ixlan: ")

print(f'\n\nRunning')

if cache_ix.lower() == 'y':
    print("Caching ix")
    ix = pdb.get_ix()
    with open('ix.json','w') as of:
        json.dump(ix["data"], of)
    print("Caching ix: Done")

if cache_net == 'y':
    print("Caching Nets")
    nets = pdb.get_net()
    with open('net.json','w') as of:
        json.dump(nets["data"], of)
    print("Caching Nets: Done")

if cache_netfac.lower() == 'y':
    print("Caching netfac")
    netfac = pdb.get_netfac()
    with open('netfac.json','w') as of:
        json.dump(netfac["data"], of)
    print("Caching netfac: Done")

if cache_netixlan.lower() == 'y':
    print("Caching netixlan")
    netixlan = pdb.get_netixlan()
    with open('netixlan.json','w') as of:
        json.dump(netixlan["data"], of)
    print("Caching netixlan: Done")


if cache_ixlan.lower() == 'y':
    print("Caching ixlan")
    ixlan = pdb.get_ixlan()
    with open('ixlan.json','w') as of:
        json.dump(ixlan["data"], of)
    print("Caching ixlan: Done")