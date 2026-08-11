# Write a functin that takes variable number of arguments and return their sum.

def calculate_multiple_nums(*args):# (*args) takes the multiple arguments whether 1 or more than 1.
    return sum(args) # actully sum() is default method in py, where it takes the parameter and additon of whole the value 
print(calculate_multiple_nums(2,3,4,5))    