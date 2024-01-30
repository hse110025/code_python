import sys
num = int(input(""))
if num==1 or num==2:
  print(4)
  sys.exit()
n=2
count=0
for i in range(1,22400):
  for j in range(1,3):
    count=j
    num-=i
    if num<1:
      if count==1:
        print(4*(i-1))
        sys.exit()
      elif count==2:
        print(4*i-2)
        sys.exit()