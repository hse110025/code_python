num = int(input(""))
total = 0
for num in range(num):
  word = input("")
  yn=5
  if len(word)==1:
    total+=1
  else:
    for i in range(1,len(word)+1):
      if len(word[i:])==1:
        yn=1
        break
      else:
        if word[i-1] in word[i:]:
          if (word[i:].index(word[i-1])) != 0:
            yn*=0
            break
        else:
          yn=1
  if yn==1:
    total+=1    
print(total)