year = int(input("enter year: "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap")
        else:
            ("not leap")
    else:
        print("leap")   
else:
    print("not leap")