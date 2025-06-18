#functions are block of code that returns specific task

#def keyword used to define a function
def hlw():
    print("Hellow world")

hlw() #calling the function

#with parameters 
def sum(a, b): #a and b is parameter here 
    addition = a+b
    return addition 
res = sum(55,45) # passing arguments with sum function
print(res)