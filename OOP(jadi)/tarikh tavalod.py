from datetime import datetime, date
date1 = date.today()
date_today=[]
date_today.append(int(date1.year))
date_today.append(int(date1.month))
date_today.append(int(date1.day))


date2=input()
date2=date2.split("/")
j=0
for i in date2:
  date2[j]=int(i)
  j += 1

if date2[1]>12 or date2[2]>31:
  print("WRONG")

else:
  date3 = (int(date_today[0]-date2[0]))
  date4 = (int(date_today[1]-date2[1]))
  date5 = (int(date_today[2]-date2[2]))
  date6 = date3 + int(((date4 * 31 + date5)/365))
  print(date6)