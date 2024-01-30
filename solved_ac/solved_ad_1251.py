import random
import math
from itertools import combinations
array = []
comparing_table=[]
word = input("")

def reverse(string):
  return_word=''
  for i in range(1,len(string)+1):
    return_word+=string[-1*i]
  return return_word

while True:
  word1=list(word)
  word1.insert(random.randint(1,len(word1)-1),'/')
  word1.insert(random.randint(1,len(word1)-1),'/')
  word2 = ''.join(word1)
  if '//' not in word2:
    array.append(word2)
  array1 = set(array)
  array = list(array1)
  if len(array)>math.comb(len(word)-1,2)-1:
    break
  
for boca in array:
  inin_num = boca.index('/')
  parta = boca[:inin_num]
  boca2 = boca[inin_num+1:]
  inin_num2 = boca2.index('/')
  partb = boca2[:inin_num2]
  partc = boca2[inin_num2+1:]
  parta = reverse(parta)
  partb = reverse(partb)
  partc = reverse(partc) 
  comparing_table.append(parta+partb+partc)

print(min(comparing_table))
  
  