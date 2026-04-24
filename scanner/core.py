# scanner/core.py

import socket
import threading
from queue import Queue
from scanner.banner import grab_banner
from scanner.utils import get_service

open_ports = []
lock = threading.Lock()
queue = Queue()

def scan_port(host, port):
    """Try connecting to a port. If open, grab banner and save."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            banner = grab_banner(sock)
            service = get_service(port)
            with lock:
                open_ports.append((port, service, banner))
        sock.close()
    except:
        pass

def worker(host):
    """Thread worker — keeps scanning ports from the queue."""
    while not queue.empty():
        port = queue.get()
        scan_port(host, port)
        queue.task_done()

def run_scanner(host, port_range=(1, 1025), num_threads=100, output=None):
    """Main scanner function — resolves host, launches threads, prints results."""
    from scanner.utils import save_results

    print(f"\n[*] Scanning {host} ...")
    try:
        ip = socket.gethostbyname(host)
        print(f"[*] Resolved to: {ip}")
        print(f"[*] Port range:  {port_range[0]} - {port_range[1]-1}")
        print(f"[*] Threads:     {num_threads}\n")
    except:
        print("[-] Could not resolve host.")
        return

    # Fill queue with ports
    for port in range(*port_range):
        queue.put(port)

    # Launch threads
    for _ in range(num_threads):
        t = threading.Thread(target=worker, args=(ip,))
        t.daemon = True
        t.start()

    queue.join()  # wait for all threads to finish

    # Print results table
    print(f"\n{'PORT':<10}{'SERVICE':<15}{'BANNER'}")
    print("-" * 55)
    for port, service, banner in sorted(open_ports):
        print(f"{port:<10}{service:<15}{banner}")
    print(f"\n[*] Scan complete. {len(open_ports)} open port(s) found.")

    if output:
        save_results(output, host, open_ports)