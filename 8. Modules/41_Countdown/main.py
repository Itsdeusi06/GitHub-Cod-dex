import datetime, bdayMessg


today = datetime.date.today()
next_bday = datetime.date(today.year, 1, 17)


if today > next_bday:  
    next_bday = datetime.date(today.year + 1, 1, 17)

days_away = next_bday - today


print(f"My next birthday is {days_away} days away!")


if days_away == 0:
    print(bdayMessg)



