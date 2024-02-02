num = int(input(""))
arr=[]
check=[]
count=0
for _ in range(num):
  contry, std_num, score = input().split(" ")
  arr.append({'contry':contry,'std_num':std_num,'score':int(score)})
arr=sorted(arr,key=lambda x:x['score'],reverse=True)
for cell in arr:
  if check.count(cell['contry']) <2:
    check.append(cell['contry'])
    print(cell['contry'],cell['std_num'])
    count+=1
    if count>2:
      break