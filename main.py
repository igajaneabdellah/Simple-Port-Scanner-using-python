#!/bin/python3

import sys
import socket
from datetime import datetime

def scan_ports(target, port_range):
    try:
        target_ip = socket.gethostbyname(target)  # Translate hostname to IPv4
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

   
    print(f"Scanning target {target_ip}")
    print("Time started:", str(datetime.now()))


    for port in range(port_range[0], port_range[1] + 1):
        scan_port(target_ip, port)

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))  # Returns an error indicator: 0 for open, otherwise non-zero
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.error:
        print(f"Could not connect to port {port}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 scanner.py <target_host> <start_port> <end_port>")
        sys.exit()

    target_host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    if start_port > end_port or start_port < 1 or end_port > 65535:
        print("Invalid port range. Port range should be between 1 and 65535.")
        sys.exit()

    scan_ports(target_host, (start_port, end_port))
