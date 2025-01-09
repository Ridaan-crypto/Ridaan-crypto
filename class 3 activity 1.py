class shoes:
    def __init__(self,brand,size,color):
        self.brand=brand
        self.size=size
        self.color=color
    def display(self):
        print(self.brand,self.size,self.color)
obj1=shoes("nike","blue","size 13")
obj1.display()
del obj1
obj1.display()