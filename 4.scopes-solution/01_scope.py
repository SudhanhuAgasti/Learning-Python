username="sudhanshu"

def func():
    # username="Agasti"//    if it is not present here it print the global value if present .
    # print(username)
    # it is print only when u call that the function !



# print(username) 
# func() 



# x = 99

# def func2(y):
#     z=x+y  # here the value of x is come from the global varibale.
#     return z

# result=func2(1)   
# print(result) 

# def func3():
#     global x   # if it is assigned by this type it print the value of inner variable.
#     x=88

# func3()
# print(x)    


# def f1():
#     x=88
#     def f2():# it print the value of the function f1()   not the outer variable. agar ea nhi hota toh ea global  space bol te  hai.
#         print("The value of the x is from the f1(): ",x)
#     return f2 

# result=f1()    
# result()



#  closure   or  factory function 
def chaicoder(num):
    def actual(x):
        return x ** num
    return  actual


def chaicoder(num):
    def actual(x):
        return x ** num
    return  actual    

f = chaicoder(2)
g = chaicoder(3)  


print(f(3))
print(g(3))

