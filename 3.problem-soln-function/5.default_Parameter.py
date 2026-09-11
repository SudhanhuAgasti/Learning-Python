# Write a function that greets a user.if no name is provided,it should greet with a default name .

name=input("Enter your name:")

def greet(name="Rahul"):
    return "Hello " + name +"!"

print(greet(name))     # Hello Rahul!  (Default value)   