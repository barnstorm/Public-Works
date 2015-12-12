#!/usr/bin/python

import sys
import time
import os
import logging
import string
import readline

bgpupdate = raw_input().split(' ')
if "announced" in bgpupdate:
    v4scope = bgpupdate[4].split('/')
    v4target_pfx = v4scope[0].split('.')
    v4pfx_len = v4scope[1]
    print v4pfx_len 
    v6map_pfx_len = int(v4pfx_len) + 64
    br_pfx = '2001:506:100:a:'
    v6target_pfx = '%s{:02X}:{:02X}{:02X}:{:02X}00::/%s'.format(*map(int, v4target_pfx))%(br_pfx, v6map_pfx_len) 
    print "neighbor 2001:db8:1:1::253 announce route {0} next-hop 2001:506:100:1::2 {1} {2} {3} {4} {5} {6}\n\r".format(v6target_pfx, bgpupdate[7], bgpupdate[8], bgpupdate[9], bgpupdate[10], bgpupdate[11], bgpupdate[12])

elif "withdrawn" in bgpupdate:
    v4scope = bgpupdate[4].split('/')
    v4target_pfx = v4scope[0].split('.')
    v4pfx_len = v4scope[1]
    v6map_pfx_len = int(v4pfx_len) + 64
    br_pfx = '2001:506:100:a:'
    v6target_pfx = '%s{:02X}:{:02X}{:02X}:{:02X}00::/%s'.format(*map(int, v4target_pfx))%(br_pfx, v6map_pfx_len)
    print "neighbor 2001:db8:1:1::253 withdraw route {0} next-hop 2001:506:100:1::2\n\r".format(v6target_pfx)
else: 
    pass
