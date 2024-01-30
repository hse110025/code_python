word = list(input(""))
comparing_table=[]
def find_the_way(word,num):
  word_len = len(word)
  range_len = word_len-num
  if range_len<1:
    return word_len
  else:
    index_num = word.index(min(word[:range_len]))
    return index_num

def reverse(string):
  return_word=''
  for i in range(1,len(string)+1):
    return_word+=string[-1*i]
    
  return return_word
def the_course(word):
  index_num = find_the_way(word,2)
  parta=word[:index_num+1]
  word = word[index_num+1:]
  index_num = find_the_way(word,1)
  partb = word[:index_num+1]
  partc = word[index_num+1:]
  parta = reverse(parta)
  partb = reverse(partb)
  partc = reverse(partc)
  return (parta+partb+partc)

wordn=word
wordnn=word
min_num = []
min_word=''

comparing_table.append(the_course(word))

while True:
  min_num.append(wordn.index(min(wordn)))
  min_word+=min(wordn)
  print(f"min_num={min_num}, min_word={min_word}, word = {wordn[:len(min_word)]+wordn[len(min_word)+1:]}")
  if(len(wordn[len(min_word)+1:])<2):
    #comparing_table.append(min_word+wordn[len(min_word):])
    break
  else:
    plus_word = the_course(wordn[:len(min_word)]+wordn[len(min_word)+1:])
    if len(plus_word)+len(min_word) == len(word):
      comparing_table.append(min_word+plus_word)
  print("-------")


print(comparing_table)
print(min(comparing_table))

##################################################################################################
'''
word = list(input(""))
comparing_table=[]
def find_the_way(word,num):
  word_len = len(word)
  range_len = word_len-num
  index_num = word.index(min(word[:range_len]))
  return index_num

def reverse(string):
  return_word=''
  for i in range(1,len(string)+1):
    return_word+=string[-1*i]
  return return_word

def the_course(word):
  index_num = find_the_way(word,2)
  parta=word[:index_num+1]
  word = word[index_num+1:]
  index_num = find_the_way(word,1)
  partb = word[:index_num+1]
  partc = word[index_num+1:]
  
  parta = reverse(parta)
  partb = reverse(partb)
  partc = reverse(partc)
  return (parta+partb+partc)

wordn=word
wordnn=word
min_num = []
min_word = '!'
for i in range(len(word)-2):
  comparing_table.append(the_course(wordn))
  min_word=min(word)
  min_num.append(wordn.index(min(wordn)))
  if wordn[min_num[-1]] == min_word:
     wordn[min_num[-1]]= '~'
     else
  print(wordn)
  comparing_table.append(the_course(wordn))
  min_num.append(wordn.index(min(wordn)))
  wordn=word
  wordn[min_num[-1]] = '~' 

comparing_table.append(the_course(word))
print((the_course(word)))
print(comparing_table)
print(min(comparing_table))

'''