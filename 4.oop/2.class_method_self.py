# Qn> add a method to the car class that display the ful name of the car(brand and model).

class Car:  # class name alawyas capital letter
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

    def full_name(self):
        return f"{self.brand} {self.model}"   


my_car= Car("Toyata","Corola")   
print("The brand of the car is : ",my_car.brand)
print("The model of the car is :",my_car.model)
print("The full name  of the car is :",my_car.full_name())


