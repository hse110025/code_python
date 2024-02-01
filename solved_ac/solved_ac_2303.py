num = int(input(""))
total=[]
def process(a):
  maxi=0
  num=a[0]+a[1]+a[2]
  num=int(str(num)[-1])
  if num>maxi:
    mini=num
  num=a[0]+a[1]+a[3]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[0]+a[1]+a[4]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[0]+a[2]+a[3]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[0]+a[2]+a[4]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[0]+a[3]+a[4]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[1]+a[2]+a[3]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[1]+a[2]+a[4]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[1]+a[3]+a[4]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  num=a[2]+a[3]+a[4]
  num=int(str(num)[-1])
  if num>maxi:
    maxi=num
  maxi=str(maxi)
  maxi=maxi[-1]
  return int(maxi)
for i in range(num):
  a= list(map(int,input("").split(" ")))
  total.append(process(a))
max_num = max(total)
if total.count(max_num)==1:
  print(total.index(max_num)+1)
else:
  reverse = [i for i in reversed(total)]
  print(len(reverse)-(reverse.index(max_num)))