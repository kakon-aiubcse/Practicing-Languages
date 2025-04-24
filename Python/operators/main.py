#arithmetic operator 

a = 7
b = 2

print(a+b) #sum of two digit
print(a-b) #sub of two digit
print(a*b) #multiplication
print(a/b) #division
print(a%b) #reminder
print(a**b) #a to the power b 
print(a^b) #bitwise XOR a = 7 so 0111 b = 0010 xor: 0101 so 4+1 = 5


#relational operator
#returns boolean either true or false 

print(a == b) #false
print(a!=b) #true
print(a>=b) #true
print(a<=b)# false
print(a>b) #true
print(a<b) #false

#assignment operator

a = 5
a = a+5
print(a) #10

a += 10
print(a) #20

a *= 5
print(a) #20 * 5 = 100
a /=5 
print (a) #100 /5 = 20

a**= 5 
print(a) #20 to the power 5 =3200000

#logical operator
#and or not

#not 
a = 5
b = 4
print(not (a==b)) # not prints opposite of true value here a and b isn't same that's why a==b is false and not oprt is true

val = True
print(not val)

#AND 
# requires two operator to be true else false 

print((not (a==b))and (val)) #both value returns true so and will display true in return

#OR
# requires one operator to be true to display true 
print((a ==b)or (val)) # one true one false result will be true