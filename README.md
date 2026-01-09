# Project 2026: Network Intelligence & Defense Suite
**Role Focus:** SOC Analyst / Network Security Engineer

## 🛠 Tools Developed
### 1. ARP Network Sweeper (`sweeper.py`)
- **Function:** Layer 2 discovery of active hosts using ARP requests.
- **SOC Use Case:** Identifying "Shadow IT" or unauthorized devices joining the subnet.

### 2. Stealth SYN Mapper (`stealth_scan.py`)
- **Function:** TCP Half-Open scanning to map service ports without completing the 3-way handshake.
- **SOC Use Case:** Mapping the attack surface of an internal asset.

### 3. SMB Security Shield & Logger (`shield.py`)
- **Function:** Monitors network traffic for port scanning activity and generates real-time security logs.
- **SOC Use Case:** Identifying reconnaissance phases of an attack. Detecting an adversary before they launch a full exploit.

## 🚀 Setup & Requirements
- **Language:** Python 3.10+
- **Library:** Scapy
- **Permissions:** Requires `sudo` or Administrator privileges for raw packet crafting.

## ⚠️ Legal Disclaimer
This toolkit is for authorized security testing and educational purposes only. Unauthorized scanning of networks you do not own is illegal.