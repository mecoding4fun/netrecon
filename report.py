from db import get_latest_scan, get_previous_state
from datetime import datetime


def generate_report(ip):
    latest = get_latest_scan(ip)
    previous = get_previous_state(ip)

    lines = []
    lines.append(f"Network Security Report")
    lines.append(f"Target IP: {ip}")
    lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 40)

    exposed = []
    changes = []

    for port, service, state, risk, ts in latest:
        if state == "open":
            exposed.append((port, service, risk))

        old_state = previous.get(port)
        if old_state and old_state != state:
            changes.append((port, old_state, state))

    if exposed:
        lines.append("\nOpen Services:")
        for port, service, risk in exposed:
            line = f"- Port {port} ({service})"
            if risk:
                line += f" | Risk: {risk}"
            lines.append(line)
    else:
        lines.append("\nNo open services detected.")

    if changes:
        lines.append("\nChanges Since Last Scan:")
        for port, old, new in changes:
            lines.append(f"- Port {port}: {old} → {new}")
    else:
        lines.append("\nNo changes detected since last scan.")

    lines.append("\nEnd of report.")
    return "\n".join(lines)
