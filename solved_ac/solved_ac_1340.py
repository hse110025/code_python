month_name=['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_date1=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_date2=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
k = input()
k=k.replace(',','')
k=k.replace(':',' ')
k=k.split(" ")
month=month_name.index(k[0])
date=int(k[1])
year=int(k[2])
hour=int(k[3])
min=int(k[4])

if (year%400==0 or (year%4==0 and year%100!=0)):
  time = (sum(month_date2[:month])+(date-1))*24*60 +hour*60+min
  print((time/(366*24*60))*100)
else:
  time = (sum(month_date1[:month])+(date-1))*24*60 +hour*60+min
  print((time/(365*24*60))*100)


