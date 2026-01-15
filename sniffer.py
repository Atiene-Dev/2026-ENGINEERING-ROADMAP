from scapy.all import sniff, IP, TCP, UDP

# This is the function that handles each packet
def process_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        
        # Checking for TCP or UDP
        if packet.haslayer(TCP):
            p_type = "TCP"
        elif packet.haslayer(UDP):
            p_type = "UDP"
        else:
            p_type = "IP"

        # Printing the result
        print(f"[FOUND] {p_type}: {src} -> {dst}")

# This part is at the margin (no spaces)
print("--- Starting 20-Packet Test ---")
sniff(prn=process_packet, store=0, count=20)
print("--- Test Finished Successfully ---")