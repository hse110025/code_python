import sys
string = input()
start_with=string[0]
if len(string)<1:
  print(-1)
  sys.exit()
process = 1
ans_string=[]
ans=[]


def assign_the_string(string,chrr):
  name = string.replace(chrr," ")
  name = name.split(" ")
  name = " ".join(name).split()
  return name

def guess_the_alphabet(cell):
  word=''
  a = len(cell)//4
  b = len(cell)%4
  if a==0:
    word+='BB'
  else:
    for count in range(a):
      word+='AAAA'
    for count in range(b):
      word+='B'
  return word

string1=assign_the_string(string,'.')
string2=assign_the_string(string,'X')

for cell in string1:
  if(len(cell)%2!=0):
    process=0
    break
  else:
    process+=1
    ans_string.append(guess_the_alphabet(cell))
    
  
if process==0:
  print('-1')
else:
  min=0
  if start_with=='X':
    if len(string2)<len(ans_string):
      for i in range(len(string2)):
        ans.append(ans_string[i])
        ans.append(string2[i])
      ans.append(ans_string[-1])
    elif len(string2)>len(ans_string):
      for i in range(len(ans_string)):
        ans.append(ans_string[i])
        ans.append(string2[i])
      ans.append(string2[-1])
    else:
      for i in range(len(ans_string)):
        ans.append(ans_string[i])
        ans.append(string2[i])
  else:
    if len(string2)<len(ans_string):
      for i in range(len(string2)):
        ans.append(string2[i])
        ans.append(ans_string[i])
      ans.append(ans_string[-1])
      
    elif len(string2)>len(ans_string):
      for i in range(len(ans_string)):
        ans.append(string2[i])
        ans.append(ans_string[i])
      ans.append(string2[-1])
    else:
      for i in range(len(ans_string)):
        ans.append(string2[i])
        ans.append(ans_string[i])
        
  ans=''.join(ans)
  print(ans)



