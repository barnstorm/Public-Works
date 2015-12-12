#!/usr/bin/env python

import sys
import time

messages = [
'announce route 1.1.0.0/24 next-hop 101.1.101.1',
'announce route 1.1.0.0/25 next-hop 101.1.101.1',
'withdraw route 1.1.0.0/24 next-hop 101.1.101.1',
]

time.sleep(2)

while messages:
    message = messages.pop(0)
    sys.stdout.write( message + '\n')
    sys.stdout.flush()
    time.sleep(1)

while True:
    time.sleep(1)
