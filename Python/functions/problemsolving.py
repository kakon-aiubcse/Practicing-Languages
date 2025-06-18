#waf to print the lenghth of a list

listingcars = ["BMW", "Toyota", "Tesla", "Honda"]

def lenoflist(list) : 
    print(len(list))

lenoflist(listingcars)

#waf to print the items inside a list

def itemsinlist(list):
    for items in list:
        print(items, end=" ")

itemsinlist(listingcars)

#WAF to print the factorial of a number 

def fact(n):
    res = 1
    for i in range(1,n+1):
        res*=i
       
    return(res)

response = fact(5)
print(response)

#WAF to convert usd to bdt 
def converter(usd):
    bdt = 125
    print("1 USD = 125 BDT", )
    res = usd*125
    print( usd, "USD ", "= ", res, "BDT")

converter(3300)
