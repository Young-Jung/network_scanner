#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    # ARP Request
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst = ip)
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    # ARP Response: return MAC Address of the IP
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    # "ff:ff:ff:ff:ff:ff" is MAC address for Broadcast
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request

    arp_request.show()
    broadcast.show()
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()

# scan("192.168.109.2")
scan("192.168.109.2/24")