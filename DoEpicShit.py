from datetime import date

today = date.today()
print("Today's date is :", today)

a = today.strftime('%d/%m/%Y')

b = a.split('/')

d,m,y = int(b[0]), int(b[1]) ,int(b[2])

time_month = ((30-d)/30)*100
time_year = ((12-m)/12)*100

hours_rem = 365*16 - ((m-1)*30*16 + d*16)

print('In this month you have ',time_month,'% time remaining for your productive work!')
print('in this year',y,', you have ',int(time_year),'% time remaining for your work')
print('In total you have ',hours_rem,'hours, equal to seeing 3 idiots',int(hours_rem/3),'times or complete',int(hours_rem/24),'days for your work!! Get up and do some shit.')
