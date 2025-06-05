#loop firstly setting up the condintion then statements then updation

i = 1 #here initialised iteration
while i <= 5: #here while keyword with condition of i is less then or equal 5 (if true it will print the statement)
    print(i)
    i+= 1 # here i += 1 means i will be increased with 1

#break works like finding the solution and closes the loop
i = 1 
while i<=10 :
    if(i == 5):
        print("complete")
        break
    i+=1

#continue keyword for terminate current iteration and pusshing to next 

i = 1 
while i<=10 :
    if(i == 5):
        print("won't print")
        i+=1
        continue
    print(i)
    i+=1

#for loops which is sequential traverse

num = [1,2,3,22]
for x in num : 
    print(num)
    
