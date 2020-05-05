#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import argparse

parser = argparse.ArgumentParser(description='Check Elasticsearch cluster health status')

parser.add_argument('--host', action='store', type=str, required=True, help='elasticsearch host')
parser.add_argument('--port', action='store', type=int, required=True, help='elasticsearch port')
parser.add_argument('--https', action='store_true', required=False, help='enable https')

args = parser.parse_args()

if args.https is True:
    schema = 'https'
else:
    schema = 'http'


def run ():
    status_checker(args.host, args.port, schema)


def status_checker(host, port, schema):
    try:
        x = requests.get(schema + "://" + host + ":" + str(port) + "/_cluster/health")
    except requests.RequestException as e:
        raise SystemExit('1')
    if x.status_code == 200:
        if x.json()['status'] == 'green':
            print('0')
        else:
            print('1')
    else:
        print('1')


if __name__ == "__main__":
    run()
