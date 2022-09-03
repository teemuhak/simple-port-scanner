# Import pyfiglet for ASCII banner
import pyfiglet
# Import sys for using sys.exit
import sys
# Import the socket module
import socket
# Import date and time
from datetime import datetime

# ASCII Banner when starting program  
ascii_banner = pyfiglet.figlet_format("SIMPLE PORT SCANNER")
print(ascii_banner)

print("DISCLAIMER: Only use this tool for targets you are allowed to scan!\n")
     
# User input for target address
target = input("Target host: ")
 
# Banner when starting scan
# Line
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
# Line
print("-" * 50)
  
try: 
    # Scan ports between 1 to 500
    for port in range(1,500):
        # New socket using the default family socket (AF_INET)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # If connection successful to target port
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
         
# Exit if keyboard interrupt         
except KeyboardInterrupt:
        print("\n Keyboard interrupt detected, terminating.")
        sys.exit()
# Exit if invalid hostname
except socket.gaierror:
        print("\n Hostname could not be resolved.")
        sys.exit()
# Exit if host not responding
except socket.error:
        print("\ Server not responding.")
        sys.exit()
