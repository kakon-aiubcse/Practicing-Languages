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

     