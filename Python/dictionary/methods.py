faculty = { 
    "name" : "abcdcutiya",
    "salary" : 24000,
    "works" : {
        "countingstudents": True,
        "gradingstudents": ['marks', 'behavior']

    }
}

#seeing all the values

print(faculty.values())


#printing all the keys 
print(faculty.keys())

#printing all key-value pairs
print(faculty.items())

#returns value based on the key
print(faculty.get('salary'))

#to add key-value pairs 
faculty.update({"position": "head"})
print(faculty)

faculty["works"].update({"istaking":True})
print(faculty)