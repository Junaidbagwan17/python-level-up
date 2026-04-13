# TODO: Write a program that converts a given number of days into years, weeks, and days

days = int(input("enter number of days:"))

total_years = days // 365
remaining_days = days % 365

weeks =  remaining_days // 7
final_days =  remaining_days % 7

print(f"{total_years} years, {weeks} weeks, {final_days} days.")