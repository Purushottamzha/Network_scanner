# scanner/banner.py

def grab_banner(sock):
    """Send a request and read the service response."""
    try:
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        return sock.recv(1024).decode(errors="ignore").strip()[:50]
    except:
        return "N/A"