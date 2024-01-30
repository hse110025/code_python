import sys
num=int(input(""))
arr=0
count=0
i=0
while True:
  i+=1
  if '666'in str(i):
    count+=1
    arr=i
    if count == num:
      print(arr)
      sys.exit()
