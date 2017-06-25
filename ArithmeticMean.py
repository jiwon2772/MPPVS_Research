#-*- coding: utf-8 -*-
file = open("C:/Users/Jayden/Desktop/drive-download-20170524T125736Z-001/test1.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)

total = float(0.0)
count = 0
check = 0
for line in file:
    lineWords = line.split()
    check = 0
    for word in lineWords:
        check+=1
        if check == 7:
            count += 1
            total += float(word)

print("total: ",total)
print("Mean:  ",total/count)

file.close()
        
