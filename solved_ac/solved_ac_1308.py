dates1 = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
dates2 = {'1':31,'2':29,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}

start_date = input().split(' ')
end_date = input().split(' ')
def distinction_a_leaf_year(y1):
  return ((y1%4==0 and y1%100!=0) or y1%400==0)
  
def count_date(data):
  calender=[1,1,1]
  total_dates=0
  for year in range(1,int(data[0])):
    if distinction_a_leaf_year(year):
      total_dates+=366
    else:
      total_dates+=365
  for month in range(1,int(data[1])):
    if distinction_a_leaf_year(int(data[0])):
      total_dates+=int(dates2[str(month)])
    else:
      total_dates+=int(dates1[str(month)])
  for datee in range(1,int(data[2])+1):
      total_dates+=1
  return int(total_dates) 
      
    
if(count_date(end_date)-count_date(start_date)>=365243):
  print("gg")
else:
  print(f"D-{count_date(end_date)-count_date(start_date)}")
