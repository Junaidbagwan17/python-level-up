# Fix the errors (get help of Google if you want but fix!)

age = input("enter age:")
if age > 20:
    print("can travel solo")
    
# TypeError: '>' not supported between instances of 'str' and 'int'
# change to  int(input("Enter age: "))    
# bcz the courrnt type is str and we want to check between numbers/int so comparing A(str) with 4(int) dosnt make sense
