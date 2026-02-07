import nmap
from db import init_db, store_results, get_previous_state
from report import generate_report


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
    init_db()
    ipinp = input("Enter ip: ")
    results = scan_ports(ipinp)
    store_results(ipinp,results)
    previous = get_previous_state(ipinp)
    report = generate_report(ipinp)
    print("\n"+ report)

    for r in results:
        old = previous.get(r["port"])
        if old and old != r["state"]:
            print(f"[CHANGE] {ipinp}:{r['port']} {old} → {r['state']}")

