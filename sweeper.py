from scapy.all import ARP, Ether, srp

#1. Create an ARP Request (Asking: "Who has this IP?")
arp_request = ARP(pdst="192.168.0.1/24")

#2. Create an Ethernet Frame (The "Megaphone" to send it to everyone)
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

#3. Combine them into one "Super packet"
combined_packet = broadcast / arp_request

print("Sweeper initialized. Ready to broadcast the subnet...")
#4. Send the combined packet and catch the answers
# we use  [0] because srp returns two lists (answered and unanswered); we only want the answered ones.
answered_list = srp(combined_packet, timeout=2, verbose=False)[0]

#5. Print the Header
print("\nTarget IP\t\tMAC Address")
print("----------------------------------------------")

#6. Loop through the results and print them
for element in answered_list:
    # element[1] is the received packet
    # .psrc is the IP of the sender, .hwsrc is the MAC address
    print(element[1].psrc + "\t\t" + element[1].hwsrc)