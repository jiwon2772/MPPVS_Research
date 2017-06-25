#-*- coding: utf-8 -*-
import ftplib
import os
from datetime import datetime
import subprocess
import time
from subprocess import check_output
import sys
#get network SSID
count = 0
wifiList = []
lists = subprocess.check_output("netsh wlan show interface")
lists = lists.decode(sys.stdout.encoding)
words = lists.split()
for curr in words:
    if curr == "SSID":
        count += 1
        continue
    if count == 2:
        wifiList.append(curr)
        count = 0
    if count > 0:
        count += 1
        continue

#connection to FTP
ftp = ftplib.FTP()
ftp.connect('185.28.21.160',int(21))
ftp.login('u742522353','qwer1234')

ftp.retrlines('LIST')
ftp.cwd('/public_html/network')

filename = 'speedtest-log-' + wifiList[0] + '.txt'

os.chdir(r'C:/Users/jayden/network')
while True:
    time.sleep(10)
    #ftp.storlines('STOR ' + filename, open(filename, 'r'))
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ts = time.time()
    print('ftp upload completed',datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

ftp.quit()

