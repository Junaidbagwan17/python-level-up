class Animal():
    def __init__(self):
        self.num_eye = 2

    def breath(self):
        print("Inhale", "exhale")

class Fish(Animal):#2
    def __init__(self):
        super().__init__()

    def breath(self):#3
        super().breath()
        print("nemo does UnderWater")

    def swim(self):
        print("Move in water")#1

nemo = Fish()
nemo.swim()
nemo.breath()

