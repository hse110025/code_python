import sys
a,b =map(int,input().split(" "))
if a<1:
  print('0')
  sys.exit()
else:
  arr =list(map(int,input().split(" ")))
  count=0
  box=0
  for i in range(len(arr)):
    box+=arr[i]
    if i<a-1 and box+arr[i+1] > b:
      count += 1
      box=0
print(count+1)
     