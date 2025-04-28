#checking a number is a multiple of 7 or not 

number = int(input("Enter number to if it is multiple of 7 or not: "))

if(number %7 == 0):
    print("The number: ",number, " is multiple of 7. ")
else:
   print("The number: ",number, " is not multiple of 7.")