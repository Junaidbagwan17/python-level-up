print("welcome to the tip calculator")

bill = int(input("what is the total bill $"))#150
tip = int(input("what percentage of tip would you like to give 10, 12 , 15% :%"))
splits = int(input("how many persons are there:")) #5

total_tip = (bill * tip ) / 100
total_bill = bill + total_tip
each_person =  total_bill / splits

print(f"your total bill is ${total_bill}, your gave ${total_tip} tip, and each person should pay ${each_person}")