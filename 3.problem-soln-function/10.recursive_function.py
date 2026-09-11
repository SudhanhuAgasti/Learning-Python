# problem==>  Create a recursive function to calculate the factorial of a number

def factorial(n):
    if(n==0):
        return 1
    else:
        return n* factorial(n-1)    
        # here the function =   factorial()   called it self.

print(factorial(5))
