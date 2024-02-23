import re
date = '28-07-2023'
outDate = '2023-07-28'
outDate2 = '07-28-23'

from datetime import datetime

# getting the current date and time
print(datetime.now())
Date=datetime.strptime(date, '%d-%m-%Y')
print(type(Date))
Datee=Date.strftime('%m-%d-%Y')
print(Datee)
print(type(Datee))
date = '28/07/2023'
date = re.sub('/','-',date)
print(date)

DatE=(datetime.strptime(date, '%d-%m-%Y').strftime('%b-%d-%y'))
print(DatE)
time_data = "25/05/99 02:35:5.523"
print(time_data.split())



