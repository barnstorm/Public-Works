
#!/usr/bin/python
import math

print """

The HD-Ratio is a way of measuring the efficiency of address
assignment [RFC 3194 ]. It is an adaptation of the H-Ratio 
originally defined in [RFC 1715 ] and is expressed as follows:

     Log (number of allocated objects)
HD = ------------------------------------------------
     Log (maximum number of allocatable objects)

where (in the case of this tool) the objects are a target IPv6 
prefix assigned from a Top Level IPv6 Aggrgate prefix of 
a given size.
"""

TLA = input("Top Level Aggregate: ")
P = input("Target Prefix: ")
AP = input("Allocated Prefixes: ")
T = math.pow(2,(P-TLA))
HD = math.log(AP)/math.log(T)

print "A %s bit Aggregate with a Target Prefix of %s allows for a maximum of %d %sbit prefixes." % (TLA, P, T, P)
print "With %s allocated prefixes and a threshold of %d total available target prefixes, the HD Ratio is %s." % (AP, T, HD)
