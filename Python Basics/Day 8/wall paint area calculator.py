test_h = int(input("enter the height:"))
test_w = int(input("enter the width:"))
coverage = 5


def paint_calc(height, width, cover):
    area = (height * width) / cover
    import math
    cans = math.ceil(area)
    print(f"you will need {cans} cans of paint.")
    
paint_calc(height=test_h, width= test_w, cover= coverage)
    