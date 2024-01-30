num=int(input(""))
count=0
for i in range(num):
  if num-i<i+1:
    break
  else:
    num-=i
    count+=1
  
print(count)