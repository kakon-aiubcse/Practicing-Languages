#problem-1 create a file using python
with open("task1.txt", "w") as f:
    data = f.write("hi everyone.\n we are learning java\n using java \n I like programming in java")
    print(data)

#Problem-2 replaces all java word with python
with open("task1.txt", "r") as f:
    data = f.read()
newdata = data.replace("java", "python")
print(newdata)

with open("task1.txt", "w") as f:
    newwritedata = f.write(newdata)


#SEARCHING A WORD IN THE FILE

word = "like"
with open("task1.txt", "r") as f:
    data = f.read()
    if (word in data):
       print("found")
    else: 
       print("not found")

#function to find line number of a word

def findingline():
    word = "like"
    ln = 1
    checking = True
    with open("task1.txt", "r") as f:
        while(checking):
            checking = f.readline()
            if(word in checking):
                print(ln)
                return
            ln+=1
    return -1

res = findingline()
print(res)