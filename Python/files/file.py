#file input and output can be done using python
#there are two types of files one is text files(.txt, .docx) another is binary(.pdf, .jpg, .mov)
#open a file do operation and close the file 

file = open("filedata.txt", "r") #open function to open a file and r is to read mode 
checkfile = file.read() #taking the data of file in a variable
print(checkfile)
print(len(checkfile))
print(type(checkfile))
file.close()

file = open("filedata.txt", "r")
checkfilefirstdata = file.readline()
checkfileseconddata = file.readline()
checkfilethirddata = file.readline()
print(checkfilefirstdata)
print(checkfileseconddata)
print(checkfilethirddata)
print(len(checkfilefirstdata))
print(len(checkfileseconddata))
print(len(checkfilethirddata))
file.close()

file = open("demowritefile.txt", "w") #w method to write
writefile = file.write("hello there")
file.close()
file = open("demowritefile.txt", "a") #a method to append 
appendfile = file.write("/n appending this line")
file.close()

#r+ is to read and write 
newfile = open("newfile.txt", "r+")
data = newfile.read()
data = newfile.write("this is a new file with read and write method r+")
newfile.close() 

#w+ is to write and overwrite

newfile = open("newfile.txt", "w+")
changeddata = newfile.write("we have changed and overright the data")
changeddata = newfile.read()
print(changeddata) #doesn't print any data
newfile.close

#a+ is to read and append data 
newfile = open("newfile.txt" , "a+") 
appendeddata = newfile.write(" lets see where it has been added")
appendeddata = newfile.read() 
print(appendeddata) #ADDED at the end but still pointer in the last
#with method 
with open("filedata.txt", "r") as k:
    data = k.read()
    print(data, "works same just different way")


#DELETE a file can be done using module like os 
import os 
os.remove("deletefile.txt")