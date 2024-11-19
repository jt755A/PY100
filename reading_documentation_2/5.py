from datetime import date

today = date.today()

today_year = today.year # year pulled from Gregorian Calendar
iso_year = today.isocalendar()[0] # returns tuple of year, week, weekday from ISO calendar

# print(today_year)
# print(iso_year)


