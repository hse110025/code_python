num = int(input(""))
mapp=[]
mapp1=[]
mapp2=[]
minkk=[]
mapp_boomb=[[0 for j in range(num+2)] for i in range(num+2)]
for i in range(num):
  string=input("")
  string=string.replace(".",'0')
  mapp.append(list(map(int,list(string))))
  mapp1.append(list(map(int,list(string))))
mapp.insert(0,[0]*(num))
mapp.append([0]*(num))
for cell in mapp:
  cell.insert(0,0)
  cell.append(0)
  
for i in range(1,num+1):
  for j in range(1,num+1):
    total=0
    total=sum(mapp[i-1][j-1:j+2])+mapp[i][j-1]+mapp[i][j+1]+sum(mapp[i+1][j-1:j+2])
    if total>9:
      mapp_boomb[i][j]='M'
    else:
      mapp_boomb[i][j]=total

mapp_boomb.pop(0)
mapp_boomb.pop(-1)
for cell in mapp_boomb:
  cell.pop(0)
  cell.pop(-1)
  mapp2.append(cell)

for i in range(num):
  for j in range(num):
    if mapp1[i][j]!=0:
      mapp2[i][j]='*'

for cell in mapp2:
  cell=list(map(str,cell))
  kk=''.join(cell)
  print(kk)
