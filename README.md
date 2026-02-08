# NetRecon

NetRecon is a lightweight local network reconnaissance and monitoring tool.  
It helps you inspect services exposed on devices within your local network, track changes over time, and generate a human‑readable security report.

The project is designed to be educational, minimal, and beginner‑friendly. It focuses on understanding what is running on your network rather than automating or exploiting it.

---

## Current Features

- TCP port scanning on common ports
- Detection of port states (open, closed, filtered)
- Identification of common services
- Risk flagging for exposed insecure services
- SQLite‑based scan history
- Change detection between scans
- Human‑readable security report generation

---

## How It Works (High Level)

1. User provides a target IP address.
2. NetRecon scans a predefined set of common TCP ports.
3. Results are stored in a local SQLite database.
4. The latest scan is compared with the previous scan for that IP.
5. A readable report is generated summarizing exposure and changes.

Scans are manual and intentional. No background automation is used.

---

## Prerequisites

- Python 3.9 or newer
- Nmap installed and available in PATH
- Access to a local network you own or are authorized to scan

Administrative privileges are not required.

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install required dependencies:

```bash
pip install scapy python-nmap
```

---

## Finding Your IP Address

You need a local IPv4 address before scanning.

### Windows
```cmd
ipconfig | findstr IPv4
```

### Linux / macOS
```bash
ifconfig | grep inet
```

Use the IPv4 address shown in the output.

---

## Running the Tool

### Device Discovery (Optional)

To scan your local network for devices:

```bash
python scan.py
```

When prompted, enter your subnet (example: `192.168.1.0`).

---

### Port Scanning & Reporting

To scan a specific device and generate a report:

```bash
python port_scan.py
```

Enter the target IP address when prompted.

The tool will:
- Scan ports
- Store results
- Detect changes
- Generate a security report

---

## Understanding the Output

During execution, NetRecon prints:
- Port number
- Service name
- Port state
- Risk description (if applicable)

After the scan, a report summarizes:
- Open services
- Risky exposures
- Changes since the last scan

If no changes are detected, this indicates a stable network state.

---

## Generated Security Report

Each run produces a plain‑text security report that includes:
- Target IP
- Scan time
- Open ports and services
- Highlighted risks
- Change summary since last scan

Reports can be viewed in the console or saved to a text file.

---

## Project Structure

- `scan.py` — Local network device discovery
- `port_scan.py` — Port scanning and change detection
- `db.py` — SQLite persistence layer
- `report.py` — Human‑readable report generation

Each component is intentionally separated for clarity.

---

## Limitations

- Scans only a limited set of common ports
- No automated scheduling
- No exploitation or attack functionality
- Intended for local and authorized networks only

This project focuses on visibility and learning, not intrusion.

---

## Ethical & Legal Notice

Only use this tool on networks and systems you own or have explicit permission to test.

Unauthorized scanning may be illegal or unethical depending on your location.  
The author is not responsible for misuse.

---

## Future Improvements

- Configurable port lists
- Report export formats
- Scan history visualization
- Optional severity scoring

These are intentionally left out to keep the project beginner‑friendly.

---

## License

This project is open‑source and intended for educational use.
