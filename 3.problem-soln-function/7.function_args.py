# Write a functin that takes variable number of arguments and return their sum.


def calculate_multiple_nums(*args):# (*args) takes the multiple arguments whether 1 or more than 1.
    # print(*args)     =2 3 4 5
    return sum(args) # actully sum() is default method in py, where it takes the parameter and additon of whole the value .


print(calculate_multiple_nums(2,3,4,5))  
print(calculate_multiple_nums(2,3,4,5,6,7,8,))    
print(calculate_multiple_nums(2,3,4,5,6,7,8,9,10,11,12,13))      