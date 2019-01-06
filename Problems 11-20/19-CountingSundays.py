year = 1900
month = 1
day = 1
dayofweek = 0
count = 0

while(1):
    day = day + 1
    dayofweek = dayofweek + 1
    if dayofweek == 7:
        dayofweek = 0
    if month == 12 and day == 32:
        year = year + 1
        day = 1
        month = 1
    if day == 32 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
        month = month + 1
        day = 1
    if day == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
        month = month + 1
        day = 1
    if year % 4 == 0 and year != 1900:
        if day == 30 and month == 2:
            month = 3
            day = 1
    else:
        if day == 29 and month == 2:
            month = 3
            day = 1
    if day == 1 and dayofweek == 6 and year > 1900:
        count = count + 1
    if day == 31 and month == 12 and year == 2000:
        break

print(count)