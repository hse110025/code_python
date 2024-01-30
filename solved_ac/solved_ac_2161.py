num=int(input(""))
arr=[]
removed_arr=[]
for i in range(1,num+1):
  arr.append(i)

for count in range(1,num):
    removed_arr.append(arr.pop(0))
    arr.append(arr.pop(0))
    
removed_arr.append(arr.pop(0))
removed_arr=map(str,removed_arr)
removed_arr=' '.join(removed_arr)
print(removed_arr)