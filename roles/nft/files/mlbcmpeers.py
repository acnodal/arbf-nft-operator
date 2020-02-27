#!/usr/bin/env python3

import sys
import yaml
import argparse


parser = argparse.ArgumentParser(description="Convert dumped metallb configmap for peer configuration using yaml variables")
parser.add_argument("--input", required=True, help="Dumped YAML using lookup k8s")
parser.add_argument("--output", required=True, help="YAML formated vars for import into ansible")

args = parser.parse_args()

try:
    with open(args.input) as f:
        data = yaml.safe_load(f)

        for i, item in enumerate(data['peers']):
            pass


        bgppeer = f"peeripaddr: {item['peer-address']} \npeerasn: {item['peer-asn']} \nmyasn: {item['my-asn']}"

        


    f.close()

    with open(args.output, 'w') as o:
         o.write('%s\n' % bgppeer )
    
    o.close


except IOError:
    print("Error input file ", args.input, " does not exist!")
    sys.exit(1)