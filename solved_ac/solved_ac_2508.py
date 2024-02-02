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
    kp=list(input(""))
    arr.append(kp)
  for i in range(row):
    if 'o' not in arr[i]:
      continue
    else:
      k = -1
      for _ in range(arr[i].count("o")):
        a=arr[i][k+1:].index('o')+1+k
        k=a
        if i!=0 and i!=row-1:
          if arr[i-1][a]=='v' and arr[i+1][a]=='^':
            count+=1
        if a!=0 and a!=col-1:
          if arr[i][a-1]=='>' and arr[i][a+1]=='<':
            count+=1
  result.append(count)
for cell in result:
  print(cell) 