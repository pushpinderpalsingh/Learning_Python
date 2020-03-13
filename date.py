from datetime import datetime,timedelta

current_date = datetime.now()

print(current_date)

one_day = timedelta(days=2)

print(current_date-one_day)
print(current_date.day)