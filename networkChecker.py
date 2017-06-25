#-*- coding: utf-8 -*-
from subprocess import check_output, STDOUT, CalledProcessError
import subprocess
import time
import sys

#get network ssid
count = 0
wifiList = []
lists = check_output("netsh wlan show interface")
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

#make command
#command = "echo $(date +'%Y-%m-%d,%H:%M'),$(../tesoeed.py -w) >> speedtest-log-" + wifiList[0] + ".txt"
file = open("C:/Users\/Jayden/network/speedtest-log-" + wifiList[0] + ".txt",mode='a',encoding='utf-8')
while True:
    #time.sleep(1)
    try :
        p = subprocess.Popen(['C:/Users/Jayden/iperf-2.0.5-cygwin/iperf.exe', '-s'],shell=True,stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
        # 3153600 seconds = about 1 month
        p2 = subprocess.Popen(['C:/Users/Jayden/iperf-2.0.5-cygwin/iperf.exe', '-c' ,'210.102.181.101','-i','1','-t','10'],shell=True,stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
        for line in iter(p2.stdout.readline, b''):
            line = line.decode(sys.stdout.encoding)
            temp = line.split()
            if len(temp) == 9:
                file = open("C:/Users\/Jayden/network/speedtest-log-" + wifiList[0] + ".txt",mode='a',encoding='utf-8')
                print(line)
                file.write(line)
                file.close()
    except Exception:
        print("Error!")
    except KeyboardInterrupt:
        print("file closed")
        file.close()
        sys.exit(0)

file.close()
