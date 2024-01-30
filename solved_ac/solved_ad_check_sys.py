import math, sys

def find_max_fac(num):
  for i in range(num+1):
    if  i in check:
      continue
    else:
      if math.factorial(i)==num:
        check.append(i)
        return math.factorial(i)
      elif math.factorial(i)>num:
        check.append(i)
        return math.factorial(i-1)

def bf(now,i):
  if i==21:
      return now==n
  a=bf(now+fac[i],i+1)
  b=bf(now,i+1)
  return a or b 
      
      
      
      
      
for num in range(1000000000000):
  n=num 
  print("\n",num)
  if num==0:
    print("1.NO")
    continue
  n = num
  check=[]

  while True:
    k=find_max_fac(n)
    if k is None:
      print("1.NO")
      break
    else:
      n-=k
      if n==0:
        print("1.YES")
        break
  if n==0:
      print("2.NO")
      continue
  fac=[1,1]
  for i in range(2,21):
      fac.append(fac[-1]*i)
  
  if bf(0,0):
      print("2.YES")
  else:
      print("2.NO")
    