#it is mainly two type one is automatic and another is manual and manual is type casting and auto is type conversation

a = 5
b = 2
sum= a+b
print(sum)

# now what if a = "5"

a = int("5") #here a has got type of integer
b = 2
sum = a+b
print(type(a))
print(sum)


#here type casting can't convert strings that doesn't carry number
a = int("kakon")

b = 5
print(a+b)