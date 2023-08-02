import subprocess
import re
# Get the list of all network interfaces
interfaces = subprocess.check_output(['ip', 'addr', 'show']).decode('utf-8')
# Find all interfaces that are connected to a router
router_interfaces = []
for line in interfaces.splitlines():
    if 'inet' in line and 'brd' in line:
        router_interfaces.append(line.split()[0])
# Get the list of all passwords for the routers
passwords = []
for interface in router_interfaces:
    # Get the password from the /etc/network/interfaces file
    password = subprocess.check_output(['cat', '/etc/network/interfaces']).decode('utf-8')
    # Find the password in the file
    match = re.search(r'password\s*=\s*(.*)', password)
    if match:
        passwords.append(match.group(1))
# Print the list of passwords
print(passwords)
