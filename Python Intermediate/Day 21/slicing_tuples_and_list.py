#LIST MANIPULATING
keys = ["a", "b" ,"c", "d", "e", "f", "g"]

print(len(keys)) #7
print(keys[2:5]) # c d e
print(keys[:5]) # a b c d e
print(keys[1:]) # b c d e f g
print(keys[::-1]) # g f e d c b a
print(keys[:: 2]) #['a', 'c', 'e', 'g']
# print(keys[start:end:step])


#NOTE: MANIPULATING tuples are same as MANIPULATING lists


# TUPLES MANIPULATING
tuple_key = ("sa", "re", "ga", "ma", "pa")

print(tuple_key[1:3]) #(re , ga)
print(tuple_key[::-1]) #('pa', 'ma', 'ga', 're', 'sa')