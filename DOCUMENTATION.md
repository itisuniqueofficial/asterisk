# 📘 Asterisk Documentation

> **Author:** Jaydatt Khodave
> **Email:** [support@itisuniqueofficial.com](mailto:support@itisuniqueofficial.com)
> **Tool:** `asterisk.py` – A low-bandwidth HTTP DoS testing script (based on Slowloris)

---

## ❓ What is Asterisk?

**Asterisk** is a stress-testing tool for HTTP/HTTPS servers using a technique known as **Slowloris attack**. It works by:

* Opening multiple connections to the server.
* Sending incomplete HTTP headers at intervals.
* Keeping connections open as long as possible to exhaust server resources.

---

## 🧪 When to Use

* For educational purposes and **authorized penetration testing only**.
* To simulate Denial-of-Service behavior in a controlled environment.
* As part of web server load testing (with legal permission).

---

## 🚀 How to Run

### 💻 Basic Usage

```bash
python3 asterisk.py <target-host>
```

Example:

```bash
python3 asterisk.py example.com
```

---

## ⚙️ Command-Line Options

| Option | Full               | Description                                               |
| ------ | ------------------ | --------------------------------------------------------- |
| `-p`   | `--port`           | Target port (default: 80)                                 |
| `-s`   | `--sockets`        | Number of simultaneous sockets (default: 150)             |
| `-v`   | `--verbose`        | Enable verbose logging                                    |
| `-ua`  | `--randuseragents` | Use a random User-Agent string for each socket            |
| `-x`   | `--useproxy`       | Route connections via SOCKS5 proxy                        |
|        | `--proxy-host`     | SOCKS5 proxy host (default: 127.0.0.1)                    |
|        | `--proxy-port`     | SOCKS5 proxy port (default: 8080)                         |
|        | `--https`          | Enable HTTPS (SSL/TLS) support                            |
|        | `--sleeptime`      | Delay (in seconds) between each header push (default: 15) |

---

## 💪 Powerful Command Examples

### 1. **Full attack on port 80 with 500 sockets**

```bash
python3 asterisk.py example.com -s 500 -p 80 -v
```

### 2. **Using HTTPS (port 443) with random user-agents**

```bash
python3 asterisk.py example.com -p 443 --https -ua -v
```

### 3. **Using a SOCKS5 proxy**

```bash
python3 asterisk.py example.com -x --proxy-host 127.0.0.1 --proxy-port 9050
```

### 4. **Slow but stealthy test (longer delay)**

```bash
python3 asterisk.py example.com -s 200 --sleeptime 30 -ua
```

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourname/asterisk.git
cd asterisk
```

2. **Install dependencies**

```bash
pip install pysocks
```

3. **Run the tool**

```bash
python3 asterisk.py <host>
```

---

## 🔒 Legal & Ethical Use

> ⚠️ **WARNING: DO NOT USE ON LIVE SERVERS YOU DO NOT OWN.**
> This script can **seriously disrupt services** and is illegal to use without **explicit permission**.

✅ You may:

* Use on **your own servers**
* Use in a **sandbox or lab environment**
* Use during **authorized pentests**

❌ You may NOT:

* Use on public websites
* Use without **explicit legal consent**
* Use for malicious or destructive purposes

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
