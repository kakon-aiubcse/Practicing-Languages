#object oriented programming in python
#class is a blueprint of a object 

class Cars:
    name= "BMW"
    price = 10

c1 = Cars() #OBJECT 
print(c1.name)

#constructor(__init__) invokes whenever a object is created of a class 
#two type of constructors one is default and another is parameterized 

class Bikes:
    #this is default
    def __init__(self):
        pass
    #this is parameterized
    def __init__(self, name , color): #Here self refers to object as bike1 
        self.name = name
        self.color = color
    showroomlocation = "Bangladesh" #this is an attribute inside a claasss and can be accessible to all instances
    #methods
    def milage(self):
        return 40

bike1 = Bikes("Honda", "black")
bike2 = Bikes("Suzuki", "Yellow")
print(Bikes.showroomlocation, bike1.milage(), bike1.color, bike1.name, bike2.name, bike2.color)
