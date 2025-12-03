row1=["🤖","🤖","🤖"]
row2=["🤖","🤖","🤖"]  
row3=["🤖","🤖","🤖"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
p = (input("value: "))

verticle = int(p[1])
horizontle = int(p[0])

map[verticle-1][horizontle-1]= "X"

print(f"{row1}\n{row2}\n{row3}")