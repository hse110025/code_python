num = int(input(""))
entry,total,count=0,0,0
for i in range(1,num+1):
  entry=i
  total=0
  while True:
    if total<num:
      total+=entry
      entry+=1
    elif total==num:
      count+=1
      break
    else:
      break
print(count)