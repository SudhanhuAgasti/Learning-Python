# create a car class with attributes like brand and model. then create an instance of this class. 
class Car:  # class name alawyas capital letter
    def __init__(self,brand,model):
        # here __init__ is constructor in the python
        self.brand= brand
        self.model= model


my_car= Car("Toyata","Corola")   
print("The brand of the car is : ",my_car.brand)
print("The model of the car is :",my_car.model)

my_new_car=Car("Tata","Safari")
print("The brand of the car is : ",my_new_car.brand)
print("The model of the car is :",my_new_car.model)