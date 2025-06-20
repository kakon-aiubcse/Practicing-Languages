#find percentage of marks of students using oop

class Student :
    def __init__(self, phy, chem , bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio
    
    @property
    def calculate(self):
        return str((self.phy+ self.bio+ self.chem)/3 )+ "%" 

s1 = Student(85,78,98)
print(s1.calculate)
s1.chem = 85
print(s1.calculate)