#!/usr/bin/env python
'''
Allows you to send multiple show commands to an XR device using NAPALM IOS/EX by changing the device driver or passing it in as an argument).

Writes the result to a file.

Not all commands will run from XML interface, failed commands will be printed to stdout along with the failure reason. These must be run manually.

This is useful for replying to TAC when they request a ton of show commands.

'''

import napalm
import sys
from pprint import pprint
from sys import argv
import requests

def napalm_connect(network_driver, mgmt_address, username, password):
    '''
    Allows you to connect to a device using Napalm
    '''
    # Load the network driver
    driver = napalm.get_network_driver(network_driver)
    
    device = driver(hostname=mgmt_address, username=username, password=password, timeout=180, optional_args={'allow_agent':'True', 'auto_rollback_on_error':'True','dest_file_system': 'bootflash:', 'global_delay_factor': 2})

    # Attempt a connection to the device
    try:
        print '\nConnecting to {}'.format(mgmt_address)
        device.open()
        return device
    except Exception as err:
        print '\nAn error occurred connecting to {}: '.format(mgmt_address)
        print type(err)
        print err
        print

def main():
    
    network_driver = 'iosxr'
    username = 'cisco'
    password = 'cisco'

    devices = ['10.4.37.16']
    cmds = ['show version','show running-config',]
#cmds = ['terminal length 0','show version','show install active','show running-config'] #DEBUG
 

    for ip in devices:
        try:
            device = napalm_connect(network_driver, ip, username, password)
            try:
                result = device.cli(cmds)
                #print result
            except Exception as err:
                print 'Failed to send command:'
                print 'ERROR: ', err
        except Exception as err:
            print 'ERROR: ', err
    
    with open('router-output.txt', 'a') as f:
        f.seek(0)
        f.truncate()
        for cmd in cmds:
            if '%' in result[cmd] and 'exec' in result[cmd] and 'not supported' in result[cmd]:
                print
                print 'Command failed: {}'.format(cmd)
                print 'Reason: {}'.format(result[cmd])
                print
                continue
            else:
                f.write('\n')
                f.write('#'*len(cmd))
                f.write('\n')
                f.write(cmd)
                f.write('\n')
                f.write('#'*len(cmd))
                f.write('\n')
                f.write(result[cmd])
                f.write('\n')
        print 'Successful commands written to {}'.format(f)
    
    device.close()        

################################    
##### OTHER NAPALM METHODS #####
################################

    # print help(device)
    # print(device.compliance_report(validation_file='validate.yml'))
    # print device.cli(['show ip int brie'])
    # print device.get_arp_table()
    # print device.get_bgp_neighbors()    
    # print device.get_bgp_config()
    # print device.get_bgp_neighbors_detail()
    # print device.get_arp_table()
    # config = device.get_config()['running']
    # print device.get_environment()
    # print device.get_interfaces()
    # print device.get_interfaces_counters()
    # print device.get_interfaces_ip()
    # print device.get_lldp_neighbors()
    # print device.get_lldp_neighbors_detail()
    # print device.get_mac_address_table()
    # print device.get_ntp_servers()
    # print device.get_ntp_stats()
    # print device.get_ntp_peers()
    # print device.get_snmp_information()
    # print device.is_alive()
    # print device.open()
    # print device.ping()
    # print device.rollback()
    # print device.traceroute()
    # print device.load_merge_candidate()
    # print device.load_replace_candidate()
    # print device.bgp_time_conversion()
    # print device.parse_uptime()
    # print device.get_firewall_policies()
    # print device.get_network_instances()
    # print device.get_probes_config()
    # print device.get_probes_results()
    # print device.get_route_to()
    # print device.get_users()
    # print device.load_template()

if __name__ == '__main__':
    main()
