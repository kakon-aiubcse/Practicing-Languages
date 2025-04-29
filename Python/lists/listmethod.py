list = ['first',2,'third']

list.append(4) #adds value in the last
print(list)
list.sort(key=str,reverse = True) #shows descending values
print(list)
list.sort(key=str)#shows ascending values
print(list)
print(list.reverse()) # displays the list in reversed form

list.insert(1, 5) #1 is index at which new element will enter and 5 is the element
print(list)
list.insert(6, "kakon")
print(list)

list.remove('kakon') #removes the items as name?
print(list)

list.pop(3) #removes the item in index 3
print(list)