#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse
import json

parser = argparse.ArgumentParser(description='Script return diff beetween remote and local last block number')


parser.add_argument('--local_node_url', action='store', type=str, required=True, help='local node url')
parser.add_argument('--remote_node_url', action='store', type=str, required=True, help='remote node url')

args = parser.parse_args()


def run ():
    remote_node_last_block = eth_block_number(args.remote_node_url)
    local_node_last_block = eth_block_number(args.local_node_url)
    diff = remote_node_last_block - local_node_last_block
    #print(str(remote_node_last_block) + "-" + str(local_node_last_block))
    print(diff)


def eth_block_number(node_url):
    try:
        url = node_url
        data = {"method": "eth_blockNumber", "params": [], "id": 1, "jsonrpc": "2.0"}
        headers = {'Content-type': 'application/json'}
        x = requests.post(url, data=json.dumps(data), headers=headers)
    except requests.RequestException as e:
        raise SystemExit('0.1')
    return int(x.json()['result'], 16)


if __name__ == "__main__":
    run()

