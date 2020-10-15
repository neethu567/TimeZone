import pytz ,datetime

year=int(input("enter year"))
month=int(input("entermonth"))
day=int(input("enter day"))
hour=int(input("enter hour"))
minute=int(input("enter minute"))

#converting to a date

users_time=datetime.datetime(year,month,day,hour,minute)
print(users_time.isoformat())

'''00 timezone for london
timezones conveersion
cairo_timezone'''

cairo_timezone=pytz.timezone('Africa/Cairo')
cairo_time=pytz.utc.localize(users_time).astimezone(cairo_timezone) #convert to utctime(london time
print("cairo_time is",cairo_time.isoformat())

#london timezone
london_timezone=pytz.timezone('UTC')#no need conersion
london_time=pytz.utc.localize(users_time).astimezone(london_timezone)
print("London_time is",london_time.isoformat())#same as utc timezme

# india timezone
delhi_timezone=pytz.timezone('Asia/Kolkata')
delhi_time=pytz.utc.localize(users_time).astimezone(delhi_timezone)
print("delhi_time is",delhi_time.isoformat())


#sydney timmezone
sydney_timezone=pytz.timezone('Australia/sydney')
sydney_time=pytz.utc.localize(users_time).astimezone(sydney_timezone)
print("sydney_time is",sydney_time.isoformat())


