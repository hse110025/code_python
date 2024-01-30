num = input("")
sets=[0]*12
for i in range(len(num)):
  sets[int(num[0])]+=1
  num=num[1:]
sets[11],sets[6],sets[9]=int((sets[6]+sets[9])/2+0.5),0,0
print(max(sets))