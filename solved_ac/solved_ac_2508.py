num = int(input(""))
result=[]
for kkp in range(num):
  num2 = input("")
  row,col=input().split(" ")
  row=int(row)
  col=int(col)
  arr=[]
  count = 0
  for i in range(row):
    k=list(input(""))
    arr.append(k)
  for i in range(row):
    if 'o' not in arr[i]:
      continue
    else:
      a=arr[i].index("o")
      if i!=0 and i!=row-1:
        if arr[i-1][a]=='v' and arr[i+1][a]=='^':
          count+=1
      if a!=0 or a!=col-1:
        if arr[i][a-1]=='>' and arr[i][a+1]=='<':
          count+=1
  result.append(count)
for cell in result:
  print(cell)    