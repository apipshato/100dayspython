age=input("what is your current age")

age_as_int=int(age)
years_remaining=90 - age_as_int
day_remaining=years_remaining * 365
week_remaining=day_remaining * 52
month_remaiinig=week_remaining * 12

message=f"you have {day_remaining} days, {week_remaining} weeks, and {month_remaiinig} month left"
print(message)
