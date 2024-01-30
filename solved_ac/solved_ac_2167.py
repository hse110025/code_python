row, col=map(int,input("").split(" "))
arr=[]
total_arr=[]
for ippp in range(row):
    ray=list(map(int,input("").split(" ")))
    arr.append(ray)
num = int(input(""))
for jppp in range(num):
  total=0
  i,j,x,y=map(int,input().split(" "))
  for k in range(i-1,x):
    for t in range(j-1,y):
      total+=arr[k][t]
  total_arr.append(total)

for cell in total_arr:
  print(cell)