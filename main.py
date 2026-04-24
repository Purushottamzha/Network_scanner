# main.py

from scanner.cli import get_args
from scanner.utils import parse_ports
from scanner.core import run_scanner

if __name__ == "__main__":
    args = get_args()
    start_port, end_port = parse_ports(args.ports)
    run_scanner(
        host=args.host,
        port_range=(start_port, end_port),
        num_threads=args.threads,
        output=args.output
    )