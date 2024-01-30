import math, sys
num = int(input(""))
if num==0:
  print("NO")
  sys.exit()
n = num
check=[]
def find_max_fac(num):
  for i in range(num+1):
    if  i in check:
      continue
    else:
      if math.factorial(i)==num:
        check.append(i)
        return math.factorial(i)
      elif math.factorial(i+1)>num:
        check.append(i)
        return math.factorial(i)
while True:
  k=find_max_fac(n)
  if k is None:
    if (n==2) and (0 not in check) and (1 not in check):
      print("YES")
      sys.exit()
    elif (n==1) and ((0 not in check) or (1 not in check)):
      print("YES")
      sys.exit()
    else:
      print("NO")
      sys.exit()
  else:
    n-=k
    if n==0:
      print("YES")
      sys.exit()
