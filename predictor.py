# bitrate optimizor
# 2017.05.07
# Jeong Jiwon / github: https://github.com/jiwon2772

#Main Algorithm function
def half_compare(start,finish,*dic):
    #half calculation
    left_amount = float(0)
    right_amount = float(0)
    print("start:%s"%start)
    print("finish:%s"%finish)
    temp_end = int(int(finish) / 2)
    temp_begin = temp_end + 1
    for i in range(start,temp_end):
        left_amount += dic_features[str(i)]
    print("left: ",left_amount)
    for i in range(temp_begin,finish):
        right_amount += dic_features[str(i)]
    print("right: ",right_amount)
    # compare left_amount and right_amount
    if left_amount >= right_amount:
        weight = 1
        if left_amount != 0 and right_amount != 0:
            weight = (left_amount/right_amount) - 1
        if weight > 1:
            weight = 1
        return weight * (left_amount / finish)
    else:
        #if left_amount
        return half_compare(start,temp_end)
    
        
#preprocessing for data
file = open("testdata.txt",mode="r",encoding="utf-8-sig",errors="strict",buffering=1)
data = file.read()
features = data.split()

start = int(1)
finish = int(1)
dic_features = {}
for feature in features:
    print(feature)
    temp = feature.split('_')
    if len(temp) > 1:
        dic_features[temp[0]] = float(temp[1])
    else:
        finish = int(temp[0])
        

file.close()

result = half_compare(start,finish,dic_features)
print("result: ",result)
