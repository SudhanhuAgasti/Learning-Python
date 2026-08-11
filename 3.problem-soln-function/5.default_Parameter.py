# Write a function that greets a user.if no name is provided,it should greet with a default name .

def greet(name="Rahul"):
    return "Hello " + name +"!"
print(greet("sudhanshu"))     #Hello sudhanshu!
print(greet())     # Hello Rahul!  (Default value)  