#problem 1
#create a student class that takes name and marks of 3 subjects as arguments of constructor and create a method to print average

class Student: 
    def __init__(self, name1, name2, name3, marks1, marks2,marks3):
        self.name1 = name1
        self.name3 = name3
        self.name2 = name2
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        print(self.name1, self.name2, self.name3, self.marks1, self.marks2, self.marks3)
    def average(self):
            sum = self.marks3+self.marks1+self.marks2
            avg = sum/3
            return avg

s1 = Student("physics", "chemisty", "math", 88,97,66)
print(s1.average())

#problem 2
#create account class with 2 attribute balance and account number
#create methods for credit , debit and printing balance

class Account :
     def __init__(self, balance, accnumber):
          self.balance = balance
          self.accnumber = accnumber
          print("Your Account Number is", accnumber)
          print("Your Balance: ",balance,"BDT")
     def debit(self, amount):
          print("you have debitted ", amount, "BDT")
          self.balance -= amount
          print("your remaining balance: ", self.balance)
     def credit(self, amount):
          print("you have credited ", amount, "BDT")
          self.balance += amount
          print("your remaining balance: ", self.balance)

ac1 = Account(17250, 424381)
ac1.debit(15000)
ac1.credit(18000)

     




#define a Circle class to create a circle with radius r using the constructor
# define an Area() method of the class which calculates the area of the circle.
# defina a perimeter () method of the class which allows you to calculate the perimeter of a circle 
#defina a employee class with attribute role, department & salary. this class also a showdetails() method 
# create an engineer class that inherits properties from employee and has additional attributes : name and age

class Circle :
     def __init__(self, radius):
          self.radius = radius
     
     def area(self):
          return ((22/7)* self.radius ** 2)
     def perimeter(self):
          return (22/7) * self.radius * 2

c1 = Circle(6)
print("Area :",c1.area())
print("perimeter :",c1.perimeter())



class Employee:
     def __init__(self, role , dept , salary):
          self.role= role
          self.dept = dept
          self.salary = salary
     def showdetails(self):
      
          print("Your role:", self.role)
          print("Your dept:", self.dept)
          print("Your salary:", self.salary)

class Engineer(Employee):
     def __init__(self, name , age):
          self.name = name
          self.age = age
          print("New engineer:",name ,"\nNew Age",  age)
          super().__init__("Engineer", "Development", "7000")


emp = Employee("Accountant", "Finance", "25000")
emp.showdetails()
eng = Engineer("Kakon", 34)
print(eng.showdetails())


#create a class which store items and price 
#use dander function __gt()___to convey that order1>order2 if price of order1>order 2

class Order:
     def __init__(self, price, name):
          self.price = price 
          self.name = name
     def __gt__(self, other):
          return self.price > other.price
     
odr1 = Order(500, "chocolate")
odr2 = Order(300, "Ice cream")
print(odr1>odr2)
