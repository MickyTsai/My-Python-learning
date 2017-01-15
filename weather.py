import daily, weekly

print('Daily Forecast:', daily.forecast())
print('Weekly Forecast:')
for number, outlook in enumerate(weekly.forecast(),1):
    print(number,outlook)
