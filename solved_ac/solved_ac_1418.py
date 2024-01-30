a = int(input(""))
b = int(input(""))

count=0

def is_it_primary(num):
    check=0
    if num//2==1:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
              check+=1
        if check > 0:
            return False
        else:
            return True

for i in range(2,a+1):
  max_num=0
  for j in range(2,i+1):
    if i%j==0 and is_it_primary(j):
      if max_num<j:
        max_num=j
  if max_num<=b and max_num>1:
    count+=1
      
print(count+1)
      
      
      