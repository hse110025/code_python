import sys
arr=input()
a=0
b=0
while True:
  if(arr[0] == "0"):
    arr=arr.lstrip("0")
    a+=1
  elif (arr[0] == "1"):
    arr=arr.lstrip("1")
    b+=1
  if len(arr)<1:
    if a<b:
      print(a)
    else:
      print(b)
    sys.exit()
