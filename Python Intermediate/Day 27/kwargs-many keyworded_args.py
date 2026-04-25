def calculate(**kwargs):
     print(kwargs)
calculate(add = 4, multiply = 6)
# # type will give you dict
print("---------------------------------")

def calculate(**kwargs):
    print("kwargs:",kwargs.items())
    print(kwargs)
calculate(add = 3, multiply = 5)
print("---------------------------------")

def calculate(**kwargs):
    print("kwargs:",kwargs)
    for key,value in kwargs.items():
        print("key:", key)
        print("value:" , value)
        print(kwargs["add"])
calculate(add = 3, multiply = 5)

print("---------------------------------")

def calculate(n, **kwargs):
    n += kwargs["add"]
    n += kwargs["multiply"]
    print("n:" , n)
calculate(2 ,add = 3, multiply = 5)

print("---------------------------------")

# **KWARGS in class

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
my_car = Car(make="Nissan", model="GT-R")
print("my_car-make:", my_car.make)
print("my_car-model:", my_car.model)
print("---------------------------------")

# we know that **kw has optional args but when we dont provide input argument it will give you error so better to use get()
# probelm:

# my_car = Car(make="Nissan") #--- here i dint provide model name so key error will occur to deal with it we use get()
# solution:
print("---------------------------------")

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
my_car = Car(make="Nissan")
print("my_car-make:", my_car.make) # here again dint give input arg still it says other args are opetional now bcz we used kw.get()
print("---------------------------------")

class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(model="Suzuki", color="white")
print(my_car.model, my_car.color)
