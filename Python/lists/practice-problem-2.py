#palindrome checking in python

list1 = [1,2,3,2,1]
list2 = [1,2,3,2,1 ]

copylist1 = list1.copy()
copylist1.reverse()

if(copylist1 == list2):
    print('palindrome')

else:
    print("not palindrome")