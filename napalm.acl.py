#!/usr/bin/env python

'''
- Allows you to send sample change to an IOS-XR device
- If changes are required these will be printed and deployed
- If no changes are required a message will be printed

'''

from napalm_base import get_network_driver


driver = get_network_driver('iosxr')
device = driver(hostname='10.4.37.16', username='cisco',
             password='cisco')


device.open()
device.load_merge_candidate(filename='ACL_SAMPLE.cfg')
diffs = device.compare_config()


if len(diffs) > 0:
    print(diffs)
    device.commit_config()


else:
    print('No changes needed')
    device.discard_config()

device.close()