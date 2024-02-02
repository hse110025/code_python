num = int(input(""))
ans=[]
for _ in range(num):
  a=input("")
  arr=[]
  arr=list(map(int,input().split(" ")))
  for i in range(arr[3]):
    arr[arr.index(max(arr[:3]))]-=1
  ans.append(arr[0]*arr[1]*arr[2])
for cell in ans:
  print(cell)