#!/usr/bin/env python
from scapy.all import *
conf.checkIPaddr=False

# configuration
localiface = 'eth1'              # your NIC name (ex)eth0, Wi-Fi)
requestMAC = ''                  # your NIC address - MAC address
myhostname=''                    # your desktop name - ex) DESKTOP-XXXXXX
localMAC = get_if_hwaddr(localiface)
requestMAC = requestMAC.replace(':','').decode('hex')

# create DHCP DISCOVER packet
ehter = Ether(src=localMAC, dst='ff:ff:ff:ff:ff:ff')
ip = IP(src='0.0.0.0', dst='255.255.255.255', ttl=128)
protocol = UDP(dport=67, sport=68)
bootp = BOOTP(op='BOOTREQUEST', flags=0, chaddr=requestMAC)
options = DHCP(options=[('message-type', 'discover'), ('client_id', chr(1),requestMAC), ('requested_addr', '0.0.0.0'), ('hostname', 'DESKTOP-8IBIVNF'), ('vendor_classs_id', 'MSFT 5.0'), ('param_req_list', chr(1), chr(3), chr(6), chr(15), chr(31), chr(33), chr(43), chr(44), chr(46), chr(47), chr(121), chr(249), chr(252)),'end'])

dhcp_discover = ehter/ip/protocol/bootp/options

print dhcp_discover.display()

# send discover, wait for reply
dhcp_offer = srp1(dhcp_discover,iface=localiface)
print dhcp_offer.display()
