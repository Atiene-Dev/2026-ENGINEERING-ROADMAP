import socket
import logging

#THIS part tells Python to write a report in a file
logging.basicConfig(filename='soc_scan.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

target = "127.0.0.1" # Scanning your own machine for safety

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    
    # 2. THE BRAIN: Deciding what is dangerous
    if result == 0:
        #This part checks if the thief is trying to get in 
        if port == 445:
            message = f"!!! CRITICAL DANGER: Port {port} (SMB) is OPEN! !!!"
        elif port == 135:
            message = f"WARNING: Port {port} (RPC) is open. Common hacker target."
        else:
            message = f"Port {port}: OPEN (DANGER!)"
        
        print(message)
        logging.warning("CRITICAL: WannaCry/SMB vulnerability detected on port 445!")
        logging.info(message) # Saves the message to your log file
    else:
        # We don't print closed ports to keep the screen clean
        pass
        
    s.close()

# 3. The list of ports a SOC Boss checks first
check_list = [22, 80, 135, 443, 445]

print(f"--- Project 2026: Scanning {target} ---")
for p in check_list:
    scan_port(p)
print("--- Scan Complete ---")