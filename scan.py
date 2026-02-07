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
    ipinp = input("Enter ip: ")
    devices = scan_network(f"{ipinp}/24")
    for d in devices:
        print(d)

