#!/usr/bin/python

import os, sys
import getopt
import subprocess

def pathExporter(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8')


os.chdir(os.path.abspath(os.path.expanduser('/Users/Luna/Desktop/p/os-path-split/')))
#for line in pathExporter('find /Users/Luna/Desktop/c'):

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:o:", ["File Path","Output File"])
except getopt.GetoptError, err:
    print str(err)
    sys.exit()

    usrPath = None
    outFile = "./default"

for o,a in opts:
    if o in ("-p","--path"):
        usrPath = a
    elif o in ("-o","--outputfile"):
        outFile = a
    else:
        assert False, "unhandled option"


print('\nCreating the <path name list> file from user input...\n')
findPath = "find " + usrPath + " > tmp.swp"
print(pathExporter(findPath))

print('\n\t tmp.swp is created. \n')

f1 = open('tmp.swp', 'r')
line = f1.readline()
while line:
    stringArr = os.path.split(line)
    f2 = file(outFile, 'a')
    f2.write(str("Directory : " + stringArr[0] + " FileName : " + stringArr[1] + "\n"))
    line = f1.readline()
f1.close()
f2.close()

os.unlink('tmp.swp')
print("\tSplit ENDED..")

