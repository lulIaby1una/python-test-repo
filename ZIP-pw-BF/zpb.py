#!/Users/Luna/.pyenv/versions/2.7.10/envs/mdev-py-2.7.10/bin/python2.7 

import zipfile
import sys
import argparse
from threading import Thread

mainparser = argparse.ArgumentParser(description='ZIP Password Cracker v1.0', prog=('zpb'))
mainparser.add_argument('-p', help='ZIP File Path')
arg1 = mainparser.parse_args()

subparser = argparse.ArgumentParser(parents=[mainparser])
subparser.add_argument('-d', help='Dictionary File Path')
arg2 = subparser.parse_args()

print('aaa')
    



