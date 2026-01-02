import socket

# This is the target (your own laptop for now)
target = "192.168.0.105"

def scan_port(port):
    #This creates a 'probe' to see if the door is open
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) #Don't wait forever
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"PORT {port}: OPEN (DANGER!)")
    else:
        print(f"PORT {port}: CLOSED (SECURE)")
    s.close()
    #The boss list of ports to check
check_list = [22, 80, 135, 443, 445]

for p in check_list:
    scan_port(p)