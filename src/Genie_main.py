from calendar import Calendar
from Genie_to_Db import GenieTodB

c = Calendar()
year = 2017
for i, month in enumerate(c.yeardayscalendar(year, width=1)): 
    for week_7 in month:
        for week in week_7:
            for date in week:
                if date == 0:
                    continue
                else:
                    #print(i+1, date)
                    if (i+1)//10 < 1:
                        si = '0'+str(i+1)
                    else:
                        si = str(i+1)
                    if date//10 < 1:
                        sdate = '0'+str(date)
                    else:
                        sdate = str(date)
                    GenieTodB(str(year)[2:]+si+sdate)                   
                    
            