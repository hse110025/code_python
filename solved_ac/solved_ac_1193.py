
'''def find_location():
  innum = int(input(""))
  total = 0
  for i in range(1,10000001):
    x=innum-total
    total+=i
    if innum <= total:
      x %=i 
      if x==0:
        x=i
      return(i,x)
      
a,b=find_location()
if a%2==0:
  y,x=(a-(b-1)),(1+(b-1))
else:
  x,y=(a-(b-1)),(1+(b-1))
print("%s/%s\n"%(x,y))'''

x=int(input())

s=0
i=0
while x>s:
    i+=1
    s+=i

s=s-i
if i%2==1:
    a=i-(x-s)+1
    b=x-s
else:
    a=x-s
    b=i-(x-s)+1

print(f'{a}/{b}')