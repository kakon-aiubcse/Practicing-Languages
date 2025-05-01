#used as pair and key like objects 
#unordered and mutable and unnamed like no similar keys 
dict = {
    "name" : "kakon",
    "age" : 45,
    "isEmployed" : False,
    "list" : [34,25,22],
    "tuples" : ('A','B'),
    23.3 : 34
    
} 
print(dict)
print(type(dict))
print(dict["list"])
dict["age"] = 35 #overwrites
print(dict["age"])
#adding new key-pair value
dict ["email"] = "kakon.aiubcse@gmail.com"
print(dict)
# creating null dictionary 
null_dict = {}
null_dict ["name"] = "khairul"
print(null_dict)