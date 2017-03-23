#!/usr/bin/python

# -*- coding : utf-8 -*-

import getopt, sys
import socket

try:
    opts, args = getopt.getopt(sys.argv[1:], "i:", ["Hostname"])
except getopt.GetoptError, err:
    print str(err)
    sys.exit()
    
host = None

print "-" * 60
for o, a in opts:
    if o in ("-i"):
        host = a
        hostIP = socket.gethostbyname(a)
        print "\tHostname \t", host
        print "\tHostIP \t\t", hostIP

print "\n\tOpened port list..."
print "-" * 60

try:
    for PORT in range(1,1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scannedResult = s.connect_ex((hostIP, PORT))

        if scannedResult == 0:
            print "\tPORT {:5}".format(PORT)
       
        s.close()

except KeyboardInterrupt:
    sys.exit()

except socket.gaierror:
    print '\nHostname cannot be resolved.\n\n'
    sys.exit()

except socket.error:
    print '\nCannot connect to Server...\n\n'
    sys.exit()


print '\nScanning Completed.\n\n'



