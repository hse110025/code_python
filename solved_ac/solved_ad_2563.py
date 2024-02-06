num = int(input(""))
a=[]
b=[]
box=[]
for i in range(num):
  k,t=input().split(" ")
  a.append([int(k),int(t)])
a=sorted(a,key=lambda x:x[0])
for i in range(num):
  b.append([a[i][0]+10,a[i][1]+10])
  
print(a)
print(b)

for i in range(len(a)):
  for j in range(len(a)):
    if (a[i][0]<=a[j][0] and a[j][0]<=b[i][0]) or (a[i][0]<=a[j][0] and a[j][0]<=b[i][0]):
      if (a[i][1]<=b[j][1] and b[j][1]<=b[i][1]):
        if i==j:
          continue
        else:
          box.append([[a[j][0],a[i][1]],[b[i][0],b[j][1]]])
          print(box)