import sys
max_price, num = map(int, sys.stdin.readline().split(" "))
name=[]
price=[]
for i in range(num):
    a = input().split(" ")
    name.append(a[0])
    price.append(int(a[1]))
mini=min(price)
maxi=max(price)
count_min_price=999999999
count_min_name=[]
for number in range(mini,maxi+1):
    counted=price.count(number)
    if counted==0:
        continue
    else:
        if counted<=count_min_price:
            if counted==count_min_price:
                count_min_name.append(number)
            else:
                count_min_name=[]
                count_min_name.append(number)
            count_min_price=counted
min_price=min(count_min_name)
print(name[price.index(min_price)],min_price)
