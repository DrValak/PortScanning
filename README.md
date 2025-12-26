# 🛡️ Port Scanner Enterprise v2.0

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Network%20Analysis-red.svg)](https://github.com)

> **Professional TCP Port Scanner** with multi-threading, logging system, JSON export, and enterprise-grade features.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Interactive Mode](#interactive-mode)
  - [Command Line Mode](#command-line-mode)
  - [Configuration File](#configuration-file)
- [Examples](#-examples)
- [Architecture](#-architecture)
- [Security & Ethics](#-security--ethics)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Port Scanner Enterprise** is a professional-grade network reconnaissance tool developed in Python. It identifies open TCP ports on target systems, maps services, and generates detailed reports in JSON format.

This tool is designed for:
- 🔍 **Network Security Audits**
- 🖥️ **Infrastructure Mapping**
- 🛡️ **Penetration Testing** (authorized only)
- 📚 **Educational Purposes** (Cybersecurity Learning)

### Key Highlights

- ⚡ **High Performance**: Multi-threaded scanning (up to 100+ concurrent threads)
- 📊 **Progress Tracking**: Real-time visual progress bar
- 📝 **Professional Logging**: Dual output (file + console)
- 💾 **JSON Export**: Structured scan results with timestamps
- ⚙️ **Configurable**: External JSON configuration file
- 🎨 **User-Friendly**: Interactive mode + CLI arguments

---

## ✨ Features

### Core Functionality

| Feature | Description |
|---------|-------------|
| **TCP Port Scanning** | Uses `socket.connect_ex()` for efficient connection testing |
| **Service Detection** | Automatically identifies services running on open ports |
| **Multi-threading** | Concurrent scanning with `ThreadPoolExecutor` |
| **Smart Timeout** | Configurable timeout (default: 1s) prevents hanging |
| **Progress Bar** | Real-time visual feedback with percentage |
| **Local IP Detection** | Automatically displays your local IP address |

### Advanced Features

- 📋 **Common Ports Mode**: Quick scan of most used ports (HTTP, HTTPS, SSH, FTP, etc.)
- 🎯 **Flexible Port Ranges**: Scan single ports, ranges (`1-1000`), or custom lists (`80,443,8080`)
- 📁 **Automatic Result Saving**: JSON files with timestamps in `scan_results/` directory
- 🔧 **Configuration File**: `config.json` for default settings
- 📊 **Detailed Reports**: Includes scan duration, target info, and service mapping
- 🧵 **Thread Control**: Adjustable thread count for performance tuning

---

## 🚀 Installation

### Prerequisites

- **Python 3.8+**
- Standard libraries only (no external dependencies!)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/PortScanning.git
cd PortScanning

# Run the scanner
python PortScanner.py
```

### First Run Setup

On first execution, the tool will create:
- `config.json` (default configuration)
- `port_scanner.log` (logging file)
- `scan_results/` (directory for JSON reports)

---

## 📖 Usage

### Interactive Mode

Simply run without arguments:

```bash
python PortScanner.py
```

You'll be prompted to enter:
1. Target IP/hostname
2. Starting port
3. Ending port

### Command Line Mode

Full control via CLI arguments:

```bash
python PortScanner.py -t <target> -p <ports> [options]
```

#### Available Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `-t, --target` | Target IP or hostname | `-t 192.168.1.1` |
| `-p, --ports` | Port range or list | `-p 1-1000` or `-p 80,443` |
| `--common` | Scan only common ports | `--common` |
| `--threads` | Number of threads | `--threads 50` |
| `--save` | Save results to JSON | `--save` |
| `--timeout` | Timeout per port (seconds) | `--timeout 2` |
| `--no-banner` | Hide local IP banner | `--no-banner` |
| `--client` | Client name for report | `--client "Acme Corp"` |
| `--project` | Project/engagement name | `--project "Q4 Security Audit"` |
| `--help` | Show help message | `--help` |

### Configuration File

Edit `config.json` to customize defaults:

```json
{
  "scan_settings": {
    "default_timeout": 1,
    "max_threads": 100,
    "default_start_port": 1,
    "default_end_port": 100
  },
  "business_info": {
    "company_name": "Your Security Consulting",
    "consultant_name": "Security Professional",
    "email": "contact@yoursecurity.com",
    "phone": "+1-XXX-XXX-XXXX",
    "website": "www.yoursecurity.com",
    "license_number": ""
  },
  "common_ports": [80, 443, 22, 21, 25, 53, 110, 143, 3306, 5432],
  "logging": {
    "enabled": true,
    "log_file": "port_scanner.log"
  },
  "output": {
    "save_results": true,
    "output_directory": "scan_results",
    "include_business_header": true
  }
}
```

---

## 💼 Professional Consulting Features

**Port Scanner Enterprise** now includes features specifically designed for independent security consultants and professionals running their own business.

### Business Configuration

Edit the `business_info` section in `config.json` to add your company details:

```json
{
  "business_info": {
    "company_name": "Your Security Consulting",
    "consultant_name": "Security Professional",
    "email": "contact@yoursecurity.com",
    "phone": "+1-XXX-XXX-XXXX",
    "website": "www.yoursecurity.com",
    "license_number": "SEC-2025-12345"
  }
}
```

### Client Reports

Generate professional reports for clients using the `--client` and `--project` flags:

```bash
python PortScanner.py -t client-server.com -p 1-1000 \
  --client "Acme Corporation" \
  --project "Q4 2025 Security Assessment" \
  --save
```

**Generated JSON Report includes:**
- Client name and project information
- Your company/consultant contact details
- Professional header with all business information
- Detailed scan results with timestamps
- Service identification

This creates client-ready reports perfect for:
- 📊 Security audit deliverables
- 📝 Penetration testing documentation
- 💼 Compliance assessments
- 🔍 Network infrastructure reviews

---

## 💡 Examples

### Example 1: Scan Localhost (Quick Test)

```bash
python PortScanner.py -t "ip" -p 1-100 --save
```

**Output:**
```
============================================================
🛡️  PORT SCANNER ENTERPRISE v2.0
🖥️  Your local IP: 
============================================================

------------------------------------------------------------
🎯 Target: 
📊 Ports: 1 - 100
🧵 Threads: 100
------------------------------------------------------------
Progress: [████████████████████] 100% (100/100)

============================================================
📋 SCAN SUMMARY
============================================================
Target: 
Ports scanned: 100
Open ports: 2
Elapsed time: 1.23s

🔓 Open ports found:
   • Port    22 - ssh
   • Port    80 - http
============================================================
✅ Results saved to: scan_results/scan_127.0.0.1_20251218_180530.json
```

### Example 2: Professional Client Scan

```bash
python PortScanner.py -t 192.168.1.100 -p 1-1000 \
  --client "TechStart Inc." \
  --project "Annual Security Audit 2025" \
  --save
```

**Output includes client information:**
```
============================================================
📋 SCAN SUMMARY
============================================================
Cliente: TechStart Inc.
Projeto: Annual Security Audit 2025
Alvo: 192.168.1.100
Portas escaneadas: 1000
Portas abertas: 5
Tempo decorrido: 12.45s
...
```

### Example 3: Scan Common Ports

```bash
python PortScanner.py -t scanme.nmap.org --common --save
```

### Example 4: Scan Specific Ports

```bash
python PortScanner.py -t example.com -p 80,443,8080,8443
```

### Example 5: Full Range Scan (Slow but Complete)

```bash
python PortScanner.py -t 192.168.1.1 -p 1-65535 --threads 200 --timeout 0.5
```

### Example 6: Interactive Mode

```bash
python PortScanner.py

# Then follow the prompts:
Digite o endereço IP ou nome do host alvo: 192.168.1.1
Porta inicial (padrão 1): 1
Porta final (padrão 100): 1000
```

---

## 🏗️ Architecture

### Code Structure

```
PortScanning/
├── PortScanner.py          # Main application
├── config.json             # Configuration file
├── port_scanner.log        # Logging output
├── scan_results/           # JSON scan reports
│   ├── scan_127.0.0.1_20251218_175359.json
│   └── scan_192.168.1.1_20251218_180542.json
├── README.md               # Documentation (English)
├── README_PT.md            # Documentation (Portuguese)
└── LICENSE                 # MIT License
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `load_config()` | Loads settings from JSON file |
| `port_scan()` | Tests single port connection |
| `scan_ports()` | Multi-threaded port range scanner |
| `save_results()` | Exports scan data to JSON |
| `validate_target()` | Validates hostname/IP |
| `get_local_ip()` | Retrieves local machine IP |

### Threading Model

```
Main Thread
    │
    ├─► ThreadPoolExecutor (max_workers=100)
    │       │
    │       ├─► Thread 1: scan_with_progress(port 1)
    │       ├─► Thread 2: scan_with_progress(port 2)
    │       ├─► Thread 3: scan_with_progress(port 3)
    │       └─► ... (up to max_threads)
    │
    └─► Lock mechanism ensures thread-safe progress updates
```

---

## ⚠️ Security & Ethics

### Legal Notice

> **⚠️ IMPORTANT**: Unauthorized port scanning may be **ILLEGAL** in many jurisdictions.

**Always ensure you have:**
- ✅ Written authorization from the system owner
- ✅ Proper scope defined in a penetration testing agreement
- ✅ Compliance with local cybersecurity laws

### Ethical Use Only

This tool is intended for:
- 🎓 Educational purposes
- 🔒 Authorized security assessments
- 🛠️ Personal network administration
- 📚 Cybersecurity research

### Disclaimer

The authors are **NOT responsible** for misuse of this software. Use responsibly and ethically.

---

## 🗺️ Roadmap

### Planned Features

- [ ] **UDP Port Scanning** support
- [ ] **Banner Grabbing** for service version detection
- [ ] **Stealth Scanning** (SYN scan using `scapy`)
- [ ] **HTML Report Generation** with charts
- [ ] **Vulnerability Database** integration (CVE lookup)
- [ ] **Network Range Scanning** (CIDR notation: `192.168.1.0/24`)
- [ ] **GUI Interface** with `tkinter` or `PyQt`
- [ ] **Email/Telegram Alerts** for monitoring mode
- [ ] **Database Storage** (SQLite) for historical tracking
- [ ] **API Endpoint** (Flask/FastAPI) for remote scanning

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by classic network tools like **Nmap**
- Built for cybersecurity education and ethical hacking practice
- Thanks to the Python community for excellent documentation

---

</div>
