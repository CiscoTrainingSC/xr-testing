#!/usr/bin/env python

'''
- Allows you to send sample change to an IOS-XR device
- If changes are required these will be printed and deployed
- If no changes are required a message will be printed
- User will be prompted to enter 'COMMIT' or 'Hit Enter' to abort
- If changes are deployed user will be prompted to enter 'ROLLBACK' to revert the change or 'Hit Enter' to keep changes

'''

from napalm_base import get_network_driver
import sys


driver = get_network_driver('iosxr')
device = driver(hostname='10.4.37.16', 
	            username='cisco', 
	            password='cisco')


device.open()
device.load_merge_candidate(filename='ACL_SAMPLE.cfg')
diffs = device.compare_config()


if len(diffs) > 0:
    print(diffs)

    commit = raw_input("Type COMMIT to commit the configuration or hit ENTER to abort: ")
    if commit == 'COMMIT':
    
        try:
            device.commit_config()

    
        except Exception as inst:
            print '\nAn error occurred with the commit: '
            print type(inst)
            sys.exit(inst)
            print
    
        else:
            print 'Config committed'
    
    else:
        sys.exit('Script aborted by user')
    
else:
    print('No changes needed')
    device.discard_config()

rollback = raw_input("Type ROLLBACK to revert changes or hit ENTER to abort: ")

if rollback == 'ROLLBACK':
    
        try:
            device.rollback()

    
        except Exception as inst:
            print '\nAn error occurred with the rollback: '
            print type(inst)
            sys.exit(inst)
            print
    
        else:
            print 'Configuration Reverted'
    
else:
    sys.exit()


device.close()