#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # ARP Request
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst = ip)
    print(arp_request.summary())
    # ARP Response: return MAC Address of the IP

# scan("192.168.109.2")
scan("192.168.109.2/24")