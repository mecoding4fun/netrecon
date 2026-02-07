# scan.py
from scapy.all import ARP, Ether, srp



def scan_network(target):
    arp = ARP(pdst=target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })
    return devices

if __name__ == "__main__":
    devices = scan_network("192.168.1.0/24")
    for d in devices:
        print(d)

