import nmap
DANGEROUS_PORTS = {
    21: "FTP (plaintext credentials)",
    23: "Telnet (no encryption)",
    445: "SMB (wormable if exposed)",
    3389: "RDP (brute-force target)"
}

def scan_ports(ip):
    scanner = nmap.PortScanner()
    ports = "21,22,23,25,53,80,443,445,3389"
    
    scanner.scan(ip, ports, arguments="-sT -T4")

    results = []

    if ip in scanner.all_hosts():
        for proto in scanner[ip].all_protocols():
            for port in sorted(scanner[ip][proto]):
                state = scanner[ip][proto][port]['state']
                service = scanner[ip][proto][port].get('name', 'unknown')

                risk = None
                if port in DANGEROUS_PORTS and state == "open":
                    risk = DANGEROUS_PORTS[port]

                result = {
                    "port": port,
                    "service": service,
                    "state": state,
                    "risk": risk
                }

                results.append(result)
                print(ip, result)

    return results


if __name__ == "__main__":
    
    ipinp = input("Enter ip: ")
    open_ports = scan_ports(ipinp)

    for p in open_ports:
        if p["state"] == "open":
            print(f"[OPEN] {p['port']} ({p['service']}) risk={p['risk']}")

