#!/usr/bin/env python3

import ipaddress
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("network", help="Supply a network range in CIDR format: 10.0.0.0/24")
group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--details", action="store_true", help="Show details for the supplied range")
group.add_argument("-l", "--list", action="store_true", help="Output a list of all ip addresses within the supplied range")
args = parser.parse_args()

try:
	network = ipaddress.ip_network(args.network)
except ValueError:
	print("That does not appear to be a valid IPv4 or IPv6 CIDR range.")
	exit()

if args.details:
	print ('CIDR Range: {}'.format(network))
	print ('Netmask: {}'.format(network.netmask))
	print ('First IP: {}'.format(network[0]))
	print ('Last IP: {}'.format(network[-1]))
	print ('Number of IPs: {}'.format(network.num_addresses))


if args.list:
	for ip in network:
		print(ip)

