import sys
if len(sys.argv) != 2:
    print("Usage:arpPing<IP>\n eg: arpPing 192.168.31.48")
    sys.exit(1)
from scapy.all import srp, Ether, ARP

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=sys.argv[1]),
                 timeout=2)
for snd, rcv in ans:
    print("Target is alive")
    print(rcv.sprintf("%Ether.src% - %ARP.psrc%"))
