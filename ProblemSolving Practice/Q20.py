# TODO: Implement a program that converts a given number of minutes into hours and minutes

total_minutes = int(input("enter total minutes:"))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{hours} Hours, {minutes} Minutes")