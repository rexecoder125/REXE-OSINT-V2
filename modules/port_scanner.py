import socket

def scan():

    target = input("Enter target IP: ")

    print("\nScanning ports (1–1024)...\n")

    for port in range(1, 1025):
        s = socket.socket()
        s.settimeout(0.3)

        try:
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
        except:
            pass

        s.close()
