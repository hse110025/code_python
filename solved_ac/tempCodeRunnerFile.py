num = int(input(""))
ans=[]
for _ in range(num):
  a=input("")
  arr=[]
  arr=list(map(int,input().split(" ")))
  arr=sorted(arr,reverse=True)
  con=arr[0]-arr[1]
  while True:
    if arr[3]<=con:
      ans.append((arr[0]-arr[3])*arr[1]*arr[2])
      break
    else:
      count=con
      arr[0]-=arr[3]    
      for i in range(arr[3]-count):
        arr[arr.index(max(arr[:3]))]-=1
      ans.append(arr[0]*arr[1]*arr[2])
for cell in ans:
  print(cell)