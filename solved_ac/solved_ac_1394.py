group=0
vsname=[]
while True:
  no=0
  p_num=int(input(""))
  if p_num==0:
    for cell in vsname:
      cell=''.join(cell)
      print(cell)
    break
  else:
    name=[]
    paper=['none']
    group+=1
    vsname.append([f"Group {group}"])
    for i in range(p_num):
      string=input().split(" ")
      name.append(string[0])
      paper.append(string[1:])
    
    for j in range(1,p_num+1):
      for k in range(p_num-1):
        if paper[j][k] =='N':
          vsname.append([f"{name[j-2-k]} was nasty about {name[j-1]}"])
        else:
          no+=1
  if no == p_num*(p_num-1):
    vsname.append(["Nobody was nasty"])
  vsname.append([""])