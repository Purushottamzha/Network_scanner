# scanner/cli.py

import argparse

def get_args():
    """Define and parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Python Port Scanner",
        usage="python main.py <host> [options]"
    )
    parser.add_argument(
        "host",
        help="Target host or IP (e.g. scanme.nmap.org)"
    )
    parser.add_argument(
        "-p", "--ports",
        default="1-1024",
        help="Port range to scan (default: 1-1024)"
    )
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=100,
        help="Number of threads (default: 100)"
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Save results to a file (e.g. -o results.txt)"
    )
    return parser.parse_args()