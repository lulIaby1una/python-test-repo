#!/Users/Luna/.pyenv/versions/2.7.10/envs/mdev-py-2.7.10/bin/python2.7 
#coding: utf-8

#####################################################################
#                                                                   #
#   Simple Web Tester v1.0                                          #
#   Edited by lullaby1una                                           #
#               2017.03.24                                          #
#                                                                   #
#####################################################################
    
import argparse
import textwrap

#args
args = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                Simple Web Tester v1.0
                -----------------------------------------------------------------------------------------------
                1   Port Scan               21 22 23 80 443 3306
                2   Search Default Page     If port 80 open, search default-page # use option  --search-default
                3   Brute Force SSH         If port 22 open, execute brute-force # use option  --brute-force
                '''))

#optional args
optional_args = args.add_argument_group('optional arguments')
optional_args.add_argument('--search-default', help='Search the default page when port 80 is opened', required=False)
optional_args.add_argument('--brute-force', help='Execute the Brute-Force attack when port 22 is opened', required=False)
optional_args.add_argument('-s','--save', help='Save the result to [path]file', required=False)
#args.parse_args(['-h'])

#required args

required_args = args.add_argument_group('required arguments')
required_args.add_argument('-T', nargs='*', help='Target Hostname',dest='host_name', required=True)

#if there have no required args
o = args.parse_args([])
#if not any([os.T]):
#    opts.print_usage()
#    exit(2)

#main

print o.host_name

port_list = [21,22,23,80,443,3306]



for i in port_list:
    print(i)
    print(type(i))
    print('norm')

args.print_usage()
