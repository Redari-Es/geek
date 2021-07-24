from scapy.all import IP, TCP, sr

ans, unans = sr(
    IP(dst="192.168.1.102") / TCP(dport=[21, 23, 135, 443, 445], flags="A"))
