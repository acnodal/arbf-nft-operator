#!/usr/bin/env python3

import sys
import json
import yaml
import argparse

lbsvcs = []

parser = argparse.ArgumentParser(description="Convert dumped k8 services to yaml variable")
parser.add_argument("--j", required=True, help="Dumped JSON file created by k8sinfo kind=Service" )
parser.add_argument("--y", required=True, help="YAML formated vars for import into ansbile")
args = parser.parse_args()

try:
    with open(args.j) as f:
        data = json.load(f)

        for i, item in enumerate(data):

            if (data[i]["spec"]["type"]) == "LoadBalancer":
                if 'ratelimit' in data[i]["metadata"]["annotations"]:
                    ratelimit = data[i]["metadata"]["annotations"]["ratelimit"]
                else:
                    ratelimit = False

                for q in data[i]["status"]["loadBalancer"]["ingress"]:
                    pass

                for p in data[i]["spec"]["ports"]:
                    pass
            

                    lbsvcs.append({'name' : data[i]["metadata"]["name"],
                                'namespace' : data[i]["metadata"]["namespace"],
                                'protocol' : p["protocol"].lower(),
                                'port' : p["port"],
                                'ipaddr' : q["ip"],
                                'ratelimit': ratelimit
                                })  


    f.close()

    with open(args.y, 'w') as o:
        o.write('loadbalancer:\n')
        yaml.dump(lbsvcs, o)
    
    o.close

except IOError:
    print("Error input file ", args.j, " does not exist!")
    sys.exit(1)









