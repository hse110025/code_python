num = int(input(""))
a=[]
b=[]
box=[]
for i in range(num):
  k,t=input().split(" ")
  a.append([int(k),int(k)+10])
  b.append([int(t),int(t)+10])
a=sorted(a,key=lambda x:x[1])
b=sorted(b,key=lambda x:x[1])
print(a)
print(b)

for i in range(num-1):
  if a[i][1]-a[i+1][0]>0:
    box.append((a[i][1]-a[i+1][0])*(b[i][1]-b[i+1][0]))
    