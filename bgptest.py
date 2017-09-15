import netmiko
from netmiko import ConnectHandler

cisco_ios_xr = {
    'device_type': 'cisco_xr',
    'ip': '10.4.37.17', #ip address of device
    'username': 'cisco', #username
    'password': 'cisco', #password
    'port': 22, # deafult is 22 #optional, not required
    'secret': 'secret', #optional, not required
    'verbose':  False, #default is Flase
}
net_connect = ConnectHandler(**cisco_ios_xr)

#send command to show the routers bgp configuration
output = net_connect.send_command('show run router bgp')
print(output)

#send command to show bgp summary
output = net_connect.send_command('show bgp summary')
print(output)

print 'Task Done' u"\U0001F37A"
