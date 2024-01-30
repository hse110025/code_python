s=sorted;print(*s(s({*open(0)})[1:],key=len),sep='')
'''
import sys

num = int(input(""))
dic=[]
dic0=[]
dic_num=[]
for i in range(num):
  boca=sys.stdin.readline().strip()
  if boca not in dic0:
    dic.append((boca,len(boca)))
    dic0.append(boca)
dic111 = sorted(dic,key=lambda x:x[0])
dictionary = sorted(dic111,key=lambda x:x[1])

for boca in dictionary:
  print(boca[0])

'''
'''
num = int(input(""))
dic=[]
dic0=[]
dic_num=[]
for i in range(num):
  boca=input("")
  if boca not in dic0:
    dic.append((boca,len(boca)))
    dic0.append(boca)
dic111 = sorted(dic,key=lambda x:x[0])
dictionary = sorted(dic111,key=lambda x:x[1])

for boca in dictionary:
  print(boca[0])
'''