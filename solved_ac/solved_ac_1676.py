import math
num=int(input(""))
fac=str(math.factorial(num))
i=len(fac)-1
while fac[i]=='0':
  i-=1
print(len(fac)-i-1)
