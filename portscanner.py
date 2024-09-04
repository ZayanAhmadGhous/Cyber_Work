import pyfiglet
import sys
import socket
from datetime import datetime

# Create an ASCII banner
ascii_banner = pyfiglet.figlet_format("SCANNER")
print(ascii_banner)

# Validate and parse command-line arguments
if len(sys.argv) == 4:
    target = socket.gethostbyname(sys.argv[1])
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
else:
    print('Usage: python scanner.py <target> <start_port> <end_port>')
    sys.exit()

# Display scanning information
print("--" * 50)
print("Scanning Target: " + target)
print("Scanning Ports from " + str(start_port) + " to " + str(end_port))
print("Start Time: " + str(datetime.now()))
print("--" * 50)

try:
    # Scan the specified range of ports
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f'Port {port} is open')
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved")
    sys.exit()
except socket.error:
    print("\nCould not connect to server")
    sys.exit()
