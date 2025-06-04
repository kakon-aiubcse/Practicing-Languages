#printing from 1 to 100 

i = 1 
while i <= 100:
    print(i)
    i += 1 

#printing from 100 to 1 

i = 100
while i >= 1:
    print(i)
    i -= 1 

#printing multiplication of a number 3
i = 1
n = 3
while i <= 10 :
    print("3", "*", i ,"=" ,n)
    i += 1
    n = 3*i

#printing traverse of a list
numbers= [1,4,9,16, 25,36 ,49,64,81,100]
i = 0
while i < len(numbers):
    print(numbers[i])
    i+=1 
#searching a number from a tuple
numbers= (1,4,9,16, 25,36,49,64,81,100)
n = 36
i = 0
while i< len(numbers):
    if(numbers[i]==n):
        print("found")
    else:
        print("not found")
    i+=1