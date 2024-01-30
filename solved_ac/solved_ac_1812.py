black=[]
grey=[]
white=[]
name=[]
while True:
  string=input("")
  if string=='#':
    break
  word1,word2=map(list,string.split(" "))
  b,g,w=0,0,0
  nama=''.join(word2)
  name.append(nama)
  for i in range(len(word1)):
    if word1[i]==word2[i]:
      b+=1
      word1[i],word2[i]='!','_'  
  for i in range(len(word1)): 
    if i < 1:
      if word2[i] in word1[:i+2]:
        g+=1
        word1[word1.index(word2[i])]='!'
        word2[i]='_'
    else:
      if word2[i] in word1[i-1:i+2]:
        g+=1
        word1[word1.index(word2[i])]='!'
        word2[i]='_'
  for i in range(len(word1)):
    if word2[i] in word1:
      w+=1
      word1[word1.index(word2[i])]='!'
      word2[i]='_'
  black.append(b)
  grey.append(g)
  white.append(w)
for k in range(len(black)):
  print("%s: %d black, %d grey, %d white"%(name[k],black[k],grey[k],white[k]))