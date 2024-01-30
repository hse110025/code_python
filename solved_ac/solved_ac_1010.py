import math
num = int(input(""))
for i in range(num):
  r,n = input("").split(" ")
  print(math.comb(int(n), int(r)))