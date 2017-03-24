#!/Users/Luna/.pyenv/versions/2.7.10/envs/mdev-py-2.7.10/bin/python2.7 
#coding: utf-8

#####################################################################
#                                                                   #
#   Simple Web Tester v1.0                                          #
#   Edited by lullaby1una                                           #
#               2017.03.24                                          #
#                                                                   #
#####################################################################

import sys
import argparse
import textwrap
import socket

#define args
args = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                Simple Web Tester v1.0
                -----------------------------------------------------------------------------------------------
                1   Port Scan               21 22 23 80 443 3306
                2   Search Default Page     If port 80 open, search default-page # use option  --search-default
                3   Brute Force SSH         If port 22 open, execute brute-force # use option  --brute-force
                '''))

args.add_argument('-T',dest='host_name', help='Target Hostname', required=False)
args.add_argument('--search-default', help='Search the default page when port 80 is opened', required=False)
args.add_argument('--brute-force', help='Execute the Brute-Force attack when port 22 is opened', required=False)

#no input required arg
opts = args.parse_args()

if not opts.host_name:
    print '\n\n'
    print args.print_help()
    print '\n\n'

    raise Exception('Required Argument Missing.')
    print '%s Program Halted.' %promptstring

#port Scanning
port_list = [21,22,23,80,443,3306]

print '-' * 60
host_ip = 
for i in port_list:
    print('norm')
