#inheritance is when one parent class is derived to its child class 

class Parent:
    def __init__(self, parentname = "father"):
        self.parentname = parentname
    
    @staticmethod
    def hello():
        print("hello world")

class Child(Parent):
    def __init__(self, parentname, childname):
        super().__init__(parentname)
        self.childname = childname
    childname = "son"

c1 = Child("father", "son")
c1.hello() #accessing parent's class's function
print(c1.parentname) #accessing parent's class attribute

c1.parentname= "son changed father's name into dad"
print(c1.parentname) #unable to fix this we have to use super method

#three types of inheritance one is single , multiple and multilevel

#single inheritance 
class A:
    print("first one")
class B(A):
    print("Class A was inherited by class B")


#multiple inheritance 
class A:
    print("first")
class B: 
    print("second")
class C(A, B):
    print("third one")

c1 = C()
print(c1)

#multi level inheritance
class A:
    print("first")
class B(A): 
    print("second inherits first")
class C(B):
    print("third inherits second")

c1 = C()
print(c1)