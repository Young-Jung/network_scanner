#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # ARP Request
    scapy.arping(ip)
    # ARP Response: return MAC Address of the IP

# scan("192.168.109.2")
scan("192.168.109.1/24")