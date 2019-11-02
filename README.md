# cidr
Print a list of ip addresses given a cidr range. 
Requires python3

```usage: cidr.py [-h] [-d | -l] network

positional arguments:
  network        Supply a network range in CIDR format: 10.0.0.0/24

optional arguments:
  -h, --help     show this help message and exit
  -d, --details  Show details for the supplied range
  -l, --list     Output a list of all ip addresses within the supplied range

$ ./cidr.py 10.0.0.0/30 -d
CIDR Range: 10.0.0.0/30
Netmask: 255.255.255.252
First IP: 10.0.0.0
Last IP: 10.0.0.3
Number of IPs: 4
$ ./cidr.py 10.0.0.0/30 -l
10.0.0.0
10.0.0.1
10.0.0.2
10.0.0.3```


