import nmap

def scan_ports(ip):
    scanner = nmap.PortScanner()
    ports = "21,22,23,25,53,80,443,445,3389"
    
    scanner.scan(ip, ports, arguments="-sT -T4")

    results = []

    if ip in scanner.all_hosts():
        for proto in scanner[ip].all_protocols():
            for port in scanner[ip][proto]:
                state = scanner[ip][proto][port]['state']
                service = scanner[ip][proto][port].get('name', 'unknown')
                print(ip,port,state,service)

                if state == "open":
                    results.append({
                        "port": port,
                        "service": service
                    })
    return results


if __name__ == "__main__":
    target_ip = "192.168.1.1"  # test on router or your own device
    open_ports = scan_ports(target_ip)

    for p in open_ports:
        print(f"Port {p['port']} ({p['service']}) is OPEN")
