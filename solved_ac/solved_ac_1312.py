a,b,n = map(int,input().split(" "))
result=0
for i in range(n):
  a%=b
  a*=10
  result=a//b
print(result)

  