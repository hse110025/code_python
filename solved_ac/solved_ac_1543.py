'''word=input("")
word2=list(word)
find=input("")
count=0
while find in word:
  idn=word.find(find)
  count+=1
  word2[idn:idn+len(find)]='!'*len(find)
  word=''.join(word2)
print(count)
'''    

sentence = input()
word = input()
num = sentence.split(word)
print(num)
print(len(num)-1)