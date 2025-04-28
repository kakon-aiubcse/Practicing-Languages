#checking the greatest number from given 3 number


number1 = int(input("Enter three number to check which one great here is Number1: "))

number2 = int(input("Enter three number to check which one great here is Number2: "))

number3 = int(input("Enter three number to check which one great here is Number3: "))

if(number1>number2 and number1>number3):
    print("The Greatest number is Number-1 : ",number1)
elif(number2>number1 and number2>number3):
   print("The Greatest number is Number-2:",number2)
else: 
    print("The Greatest number is Number-3:", number3)