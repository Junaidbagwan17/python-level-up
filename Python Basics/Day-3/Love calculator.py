print("welcome to the love calculator!")


name1 = input("Enter Name 1:").lower()
name2 = input("Enter Name 2:").lower()

combined_name = name1 + name2

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
true = t + r + u + e
l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
love = l+o+v+e

score = str(true) + str(love)

result = int(score)
if result <= 10 and result >= 90:
    print(f"You go like coke and mentos together and your love score is {score}")
elif result >= 40 or result <= 50:
    print(f"You go alright togehter and your love score is {score}")
else:
    print(f"Your love score is {score}")