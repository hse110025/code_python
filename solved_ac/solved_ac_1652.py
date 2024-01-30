num=int(input(""))
num_=0
numl=0
seatsl=[['_'for i in range(num)]for j in range(num)]
seats_=[['_'for i in range(num)]for j in range(num)]
for i in range(num):
  sss=input("")
  for j in range(len(sss)):
    seats_[i][j]=sss[j]
    seatsl[j][i]=sss[j]

for cell in seats_:
  string=''.join(cell)
  string=string.split('X')
  for roll in string:
    if len(roll)>1:
      num_+=1
for cell in seatsl:
  string=''.join(cell)
  string=string.split('X')
  for roll in string:
    if len(roll)>1:
      numl+=1
print(num_,numl)
  

