# scanner/utils.py

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

def get_service(port):
    """Return service name for a given port number."""
    return COMMON_PORTS.get(port, "Unknown")

def parse_ports(port_string):
    """Convert '1-1024' string into (1, 1025) tuple."""
    try:
        start, end = port_string.split("-")
        return int(start), int(end) + 1
    except:
        print("[-] Invalid port range. Use format: 1-1024")
        exit()

def save_results(filename, host, results):
    """Save scan results to a text file."""
    with open(filename, "w") as f:
        f.write(f"Scan results for: {host}\n")
        f.write(f"{'PORT':<10}{'SERVICE':<15}{'BANNER'}\n")
        f.write("-" * 55 + "\n")
        for port, service, banner in sorted(results):
            f.write(f"{port:<10}{service:<15}{banner}\n")
    print(f"[*] Results saved to {filename}")