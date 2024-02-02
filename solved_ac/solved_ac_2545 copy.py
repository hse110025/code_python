num = int(input(""))
ans=[]
for _ in range(num):
  a=input("")
  arry=[]
  arry=list(map(int,input().split(" ")))
  arr=sorted(arry[:3],reverse=True)
  count=0
  while True:
    arr=sorted(arr[:3],reverse=True)
    con=arr[0]-arr[1]
    if (arry[3]-count)<=con:
      ans.append((arr[0]-count)*arr[1]*arr[2])
      break
    else:
      if con!=0:
        arr[0]-=con
        count+=con
      else:
        arr[0]-=1
        count+=1
      if count>arry[3]-1:
        ans.append(arr[0]*arr[1]*arr[2])
        break
    
for cell in ans:
  print(cell)
#####3점 받고 싶.