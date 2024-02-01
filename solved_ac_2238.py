max_price, num = map(int, input().split(" "))
arr=[]
n=0
np=0
for i in range(num):
    name,price=map(str,input().split(" "))
    arr.append({'name':name,'price':int(price)})
arr=sorted(arr,key= lambda x: x['price'])
min_pri=arr[0]['price']
print(min_pri)
for i in range(1,len(arr)):
    print(arr[i+np])
    if arr[i+np]['price']==min_pri:
        np-=1
        arr.pop(i)
'''
for cell in arr:
    print(cell)
'''

"""

arr = map(arr,)
"""