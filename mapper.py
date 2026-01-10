import socket

def scan_port(ip,port):
    # 1. Create the 'socket' (like picking up a phone)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Set a timer (don't wait more than one second for a answer)
    s.settimeout(1)

    # 3. Try to connect (The 'Knock')
    # connect_ex returns 0 if it works, an error code if it doesn't
    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"[!] Port {port} is OPEN - Possible entry point!")
    else:
        print(f"[-] Port {port} is CLOSED.")
    # 4. Hang up the phone
    s.close()

    #-----Test it below-------
target = input("Enter ip to map: ")
               
print(f"---- Scanning ports 20 to 100 on {target} ---")
for port in range(20, 101):
    scan_port(target, port) 
print("Scan complete. How many 'OPEN' doors did you find?")
