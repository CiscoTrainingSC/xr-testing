import netmiko
import napalm
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

#send command show ip int brief and output
output = net_connect.send_command('show ip int brief')
print(output)

#send command with config set
output = net_connect.send_config_set(['hostname RTR-ISP-01', 'commit'])
print(output)

#send command to sh run only hostname
output = net_connect.send_command('show run | i hostname')
print(output)

