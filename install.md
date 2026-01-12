# Project 2026: SOC Suite Setup Guide

This guide explains how to set up the environment for the Sweeper, Mapper, and Shield scripts.

## 1. Prerequisites
- **Python 3.10+**: The core language used.
- **Git**: For version control.

## 2. Network Driver Setup
**Npcap** is required for the scripts to interact with network hardware.
- **Download:** https://npcap.com/
- **Note:** During installation, check the box: "Install Npcap in WinPcap API-compatible Mode."

## 3. Python Libraries
Open the terminal and run:
```bash
pip install scapy

#USAGE INSTRUCTIONS
1.Port mapper
python mapper.py
Enter target ip when prompted
scans port 20-100 for open services

2.Shield
python shield.py
monitors network for incoming connection attempts
logs result to soc_Scan log
important:always run vs code as administrator to give scripts permission to scan the network
