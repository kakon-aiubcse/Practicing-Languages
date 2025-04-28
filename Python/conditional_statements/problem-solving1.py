#grading students based on marks 

marks = int(input("Enter Marks to check grade: "))

if(marks >=90):
    print("you got A+ with",marks, "marks")
elif(marks>=80 and marks<=89):
   print("you got A with",marks, "marks")
elif(marks>=70 and marks<=79):
   print("you got B with",marks, "marks")
else:
   print("you got C with",marks, "marks")