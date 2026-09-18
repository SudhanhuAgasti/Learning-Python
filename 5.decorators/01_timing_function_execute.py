import time


# now make a  function which is use like a tool , when ever any other fucntion come it deffinetley pass thorough it.
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()  # calculate the time
        result= func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper   




# decorator by timer function like tool gate .
@timer
def example_function(n):
    time.sleep(n)

example_function(2)  
print("executed successfully through the timer function !")       
