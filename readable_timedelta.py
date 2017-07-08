"""This is a function to calculate how many weeks or days for a given duration. 
"""
def readable_timedelta(days):
    return "{} weeks(s) and {} days(s)".format(days//7, days%7)

print(readable_timedelta(10))
