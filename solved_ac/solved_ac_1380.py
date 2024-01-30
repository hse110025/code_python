scenario=0
leaf_list=[]
while True:
  p_num=int(input(""))
  name_list=['']*(p_num+1)
  check_list=['']*(p_num+1)
  if p_num==0:
      for cell in leaf_list:
        print(cell[0],cell[1])
      break
  else:
      scenario+=1
      for i in range(1,p_num+1):
        name_list[i]=(input(""))
      for j in range((2*p_num)-1):
        a,b=map(str,input().split(" "))
        check_list[int(a)]+=b
      for n in range(1,len(check_list)):
        if len(check_list[n])==1:
          leaf_list.append([scenario,name_list[n]])