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

#send command new loopback interface
output = net_connect.send_config_set(['int lo2 ip address 192.168.1.1/32', 'commit'])
print(output)

#send command to show run the new loopback
output = net_connect.send_command('sh run int lo2')
print(output)

