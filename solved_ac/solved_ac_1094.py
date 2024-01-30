num=int(input(""))
cane=64
blocks=[0]
if num==64:
  print(1)
else:
  while True:
    cane/=2
    if cane<1:
      break
    blocks.append(cane)
    blocks.append(cane)
    if(sum(blocks[:-1])>num):
        blocks.pop()
        blocks.pop()
    else:
        blocks.pop()
  print(len(blocks)-1)
        