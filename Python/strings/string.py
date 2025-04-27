#3 ways to define strings

str1 = "this is kakon with double quotation"
str2 = 'this is kakon2 with single quotation'
str3 = """this is kakon3 with triple quotation"""

#print(str1,str2,str3)

#/n for new line and /t for tab space

data = "this is kakon here.\nnothing special.\tjust learning"
print(data)
#concat 
firstname ="Khairul Islam"
secondname = "Kakon"
finalname = firstname +" "+ secondname
print((finalname[13]))
print(finalname)
print(len(finalname))
#indexing 
str = "datadatadata datadata"
print((str[2]))
print(len(str))

#'str' object does not support item assignment
#str[1] = 'D'
#print(str[1])

#slicing / indexing
print(str[1:10]) #wiil print 1 to 9
print(str[5:]) # will print from 5 to last
print(str[:5]) #will print before 6

#backword indexing
kakon = "kakon"
print(kakon[-5:])#will print kakon
print(kakon[:-1]) #will print kako
print(kakon.endswith("on")) #checks if it contains on in last
print(kakon.capitalize()) #capitalizes the first word
print(kakon.find("o")) #searches for existences and return index where it is
print(kakon.count("k")) #returns how many times k exists

