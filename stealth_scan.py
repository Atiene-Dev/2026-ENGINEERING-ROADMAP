from scapy.all import IP, TCP, sr1
import logging

# Hide annoying warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def stealth_scan(target_ip, target_port):
    print(f"\n--- Scanning {target_ip} on port {target_port} ---")
    
    # S = SYN (The 'Can we talk?' knock)
    packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")
    
    # Send and wait for response
    response = sr1(packet, timeout=2, verbose=0)
    
    if response is None:
        print(f"RESULT: Port {target_port} is FILTERED (The router is hiding/ignoring us).")
    elif response.haslayer(TCP):
        # 0x12 = SYN-ACK (The 'Yes, I'm here!' answer)
        if response.getlayer(TCP).flags == 0x12:
            print(f"RESULT: Port {target_port} is OPEN! (Service is active)")
            # Send Reset to close the connection stealthily
            sr1(IP(dst=target_ip)/TCP(dport=target_port, flags="R"), timeout=1, verbose=0)
        # 0x14 = RST-ACK (The 'Go away!' answer)
        elif response.getlayer(TCP).flags == 0x14:
            print(f"RESULT: Port {target_port} is CLOSED.")

# REPLACE THE IP BELOW WITH YOUR 'DEFAULT GATEWAY'
router_ip = "192.168.0.1" 

# We are testing Port 80 (The Router's Login Page)
stealth_scan(router_ip, 53)