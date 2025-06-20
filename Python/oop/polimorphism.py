#polymorphism is like many forms like same name of methods but different in different classes

#polymorphism operator overloading

class twoD:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
    
    def __add__(self, other):
        return twoD(self.a1 + other.a1 ,  self.a2+ other.a2)
     
    def __str__(self):  # Enables nice print()
        return f"twoD({self.a1}, {self.a2})"
    
sum1 = twoD(20,25)
sum2 = twoD(35,40)
newsum = sum1+sum2
print(newsum)