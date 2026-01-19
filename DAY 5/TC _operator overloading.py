class box1:
    def __init__(self,value):
        self.value = value
    def add(self,other):
        return self.value + other.value

b1=box1(50)
b2=box1(30)
print(b1.add(b2))
