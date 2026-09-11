# Functionn with **kwargs

# problem : Create a function that accepts any number of keyword arguments and prints them in the format key:value : 

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        # f    is the formatting string here !


print_kwargs(name="Ajay tiwari ",power="lazer")
print_kwargs(name="Sudhanshu ")
print_kwargs(name="Rahul ",power="Aleexr",enmy="Dr. Jackal")



