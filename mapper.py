import socket

def scan_port(ip, port):
    # This sets up the 'phone line' to talk to the other computer
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
    # This 'knocks' on the door (port)
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"[!] Port {port} is OPEN!")
        try:
            # We ask the server for its 'ID Card' (Banner)
            s.send(b"Hello\r\n")
            banner = s.recv(1024)
            print(f"    [Service Info]: {banner.decode().strip()}")
        except:
            print("    [Service Info]: Service detected but no banner received.")
    else:
        # If the knock gets no answer
        print(f"[-] Port {port} is closed.")
    
    s.close()

# --- THE STARTING POINT ---
target = input("Enter IP to map (e.g., 192.168.0.1): ")
print(f"--- Scanning ports 20 to 100 on {target} ---")

# This loop automatically checks ports 20 through 100
for port in range(20, 101):
    scan_port(target, port)

print("Scan complete. Good job, Engineer.")