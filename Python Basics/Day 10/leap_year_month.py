print("Leap Year or Not Leap Year")

year = int(input("enter year: "))
month = int(input("Enter a month"))

def is_leap(year):
    if year % 4 == 0: #leap
        if year % 100 == 0: # leap
            if year % 400 == 0:#leap 
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year , month):
    month_days= [31 , 28, 31, 30, 31,30,31,30,31,30,31, 30]
    if is_leap(year) and month == 2:
        return 29
    return  month_days[month-1]

day = days_in_month(year , month)
print(day)