from operator import length_hint
n,m=map(int,input().split(" "))
moja=[[0 for j in range(101)]for i in range(101)]
boja=[]
total=0
for i in range(n):
  x1,y1,x2,y2=map(int,input().split(" "))
  for j in range(x1,x2+1):
    for k in range(y1,y2+1):
      moja[j][k]+=1
for j in range(101):
  for k in range(101):
    if(moja[j][k]>m):
      total+=1
print(total)
      
      
'''for cell in moja:
  print(cell)

for k in range(101):
  boja.append (list(map(lambda x: [k,x],list(filter(lambda x: moja[x][k] >m ,range(101))))))
boja=(list(filter(lambda x:len(x)>0,boja)))

for i in range(len(boja)):
  total+=len(boja[i]) 
print(total)'''
