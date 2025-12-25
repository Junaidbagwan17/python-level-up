# Play computer and read lines

year = input("enter birth year:")
if year > 1980 and year  < 1994:
    print("You are Millneial")
elif year > 1994:
    print("Gen z")

# here we see nothing when we print 1994 becz there it has bountrys []
# when you 1994 and it should print millenal but not printing anyhing
# so we need operator check
# also year has no int()
# solution

year = int(input("enter birth year:"))
if year >= 1980 and year  >=  1994:
    print("You are Millneial")
elif year > 1994:
    print("Gen z")