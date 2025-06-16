# `asterisk.py` – Simple Low-Bandwidth DoS Tool in Python

## What is Asterisk?

**Asterisk** is a low-bandwidth HTTP Denial of Service attack tool that targets threaded web servers.

It works like this:

1. It opens multiple connections to the target HTTP server.
2. It keeps these connections alive by sending partial HTTP headers at regular intervals.
3. It never completes the request, which ties up the server’s resources and prevents it from serving legitimate users.

This simple technique can exhaust the server’s thread pool, making it unresponsive to real traffic.

---

## Citation

If you find this tool useful in your testing, please cite it as:

```bibtex
@software{khodave2025asterisk,
  title = {Asterisk},
  author = {Jaydatt Khodave},
  year = {2025},
  note = {Low-bandwidth HTTP DoS tool},
  url = {https://github.com/yourname/asterisk}
}
```

(Replace `yourname` with your actual GitHub username if publishing.)

---

## Installation & Usage

You can clone the GitHub repo and run the script using Python 3.

### Install dependencies

```bash
pip install pysocks
```

### Clone and run

```bash
git clone https://github.com/yourname/asterisk.git
cd asterisk
python3 asterisk.py example.com
```

---

### SOCKS5 Proxy Support

If you'd like to route your traffic through a **SOCKS5 proxy**, you must install `PySocks` (a fork of SocksiPy).

```bash
pip install pysocks
```

Then run:

```bash
python3 asterisk.py example.com -x --proxy-host 127.0.0.1 --proxy-port 9050
```

---

## Command-Line Options

You can customize Asterisk’s behavior via CLI arguments:

| Option                    | Description                                         |
| ------------------------- | --------------------------------------------------- |
| `-p`, `--port`            | Port to target (default: 80)                        |
| `-s`, `--sockets`         | Number of concurrent sockets (default: 150)         |
| `-v`, `--verbose`         | Enable verbose logging                              |
| `-ua`, `--randuseragents` | Use random User-Agent headers                       |
| `-x`, `--useproxy`        | Use SOCKS5 proxy for connections                    |
| `--proxy-host`            | Host of the SOCKS5 proxy (default: 127.0.0.1)       |
| `--proxy-port`            | Port of the SOCKS5 proxy (default: 8080)            |
| `--https`                 | Enable HTTPS support                                |
| `--sleeptime`             | Time (in seconds) to sleep between each header sent |

Run `python3 asterisk.py -h` for full help.

---

## License

This project is licensed under the **MIT License**.

---

> ⚠️ **DISCLAIMER**:
> This tool is designed for **educational and authorized penetration testing only**.
> Do **not** use Asterisk against servers you do not own or explicitly have permission to test.
> Unauthorized use is **illegal** and can result in criminal prosecution.
