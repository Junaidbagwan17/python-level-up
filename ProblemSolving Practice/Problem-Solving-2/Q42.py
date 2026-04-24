# todo: Implement a function to check if a given year is a leap year or not
# Leap when and when not:
# Divisible by 4 ✅
# BUT if divisible by 100 ❌
# EXCEPT if divisible by 400 ✅

def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("enter a year:"))
result = check_leap_year(year)

if result: # == True
    print("Leap year")
else:
    print("not a leap year")