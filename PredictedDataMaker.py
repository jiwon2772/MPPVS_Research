# This module is for making a data of throughput prediction
# developed by Jayden Jeong
# jiwon2772@naver.com
# 2017-05-14
import sys
import ftplib
import subprocess

def main(argv):
    if len(argv) > 1:
        print("#Parameter error: This module need only one argument!")
    else:
        dataMaker(argv[0])
        
def dataMaker(num):
    num = int(num)
    result = []
    count = 0
    isChecked = False
    curr_ssid = ""
    wifiList = {}

    # scanf all visible wifi to check signal strength
    lists = subprocess.check_output("netsh wlan show network mode=bssid")
    lists = lists.decode(sys.stdout.encoding)
    words = lists.split()
    for curr in words:
        if curr == "SSID":
            count += 1
            continue
        if curr == "Signal" and isChecked :
            count += 1
            continue
        if count == 2:
            if isChecked == False:
                count += 1
                continue
            else:
                wifiList[curr_ssid] = curr
                isChecked = False
                count = 0
        if count == 3:
            if isChecked == False:
                wifiList[curr] = "0%"
                curr_ssid = curr
                isChecked = True
                count = 0
        if count > 0:
            count += 1
    
    print(lists)
    print("\n")
    print(wifiList)
    
    
    
    checkLTE()

    #for i in range(0,num):
        
def checkLTE():
    path = "/public_html/network"
    filename1 = "speedtest-log-aimhigh.txt"
    filename2 =  ""

    ftp = ftplib.FTP()
    ftp.connect('185.28.21.160',int(21))
    ftp.login('u742522353','qwer1234')

    ftp.cwd(path)
    ftp.retrbinary("RETR " + filename1, open(filename1, 'wb').write)

    ftp.quit()



    
if __name__ == "__main__":
    main(sys.argv[1:])
