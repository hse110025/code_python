candidates = int(input(""))
candidates_score=[]
count=0
for i in range(candidates):
  candidates_score.append(int(input("")))
candidate = candidates_score[0]
candidates_score[0]=-999
while True:
  if len(candidates_score)<2:
    print('0')
    break
  else:
    if candidate>max(candidates_score[1:]):
      print(count)
      break
    else:
      count+=1
      candidates_score[candidates_score.index(max(candidates_score[1:]))]-=1
      candidate+=1
   
   