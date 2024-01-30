num=list(map(int,input("")))
count=0
while len(num)>1:
  total=str(sum(num))
  num=list(map(int,total))
  count+=1
print(count)
num=map(str,num)
gum=''.join(num)
if(int(gum)%3==0):
  print('YES')
else:
  print('NO')
