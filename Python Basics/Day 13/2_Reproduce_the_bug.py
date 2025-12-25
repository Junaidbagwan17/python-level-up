# Reproduce the bugs
from random import randint

dice_img = ["1️⃣","2️⃣", "3️⃣","4️⃣","5️⃣","6️⃣"]
dice_num = randint(0,6-1)
print(dice_img[dice_num])

# IndexError: list index out of rang

# here when we are trying to print the images 1 to 6 with we got error sometime
# bcz when list index start from 0 so we have stated random int which has no 0 a and no 6 thats why itgave error
# so if we change the randint(0 , len(img)-1) or (0,5) it will print propely 
# also if you do (1, to 6-1) it will start from second imag and first image will print never and also give not error this is the big gap
# doing (0 , 5) is the best way to handle or(0, 6-1)