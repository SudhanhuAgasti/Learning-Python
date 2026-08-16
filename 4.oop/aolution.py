class Car:
    def __init__(self,brand,model):
        # here __init__ is constructor in the python
        self.brand= brand
        self.model= model

    def fullName(self):
        # self.istname=istname
        # self.last_name=last_name
        return f"{self.brand}{self.model}"

class ElectricCar(Car):# inherit from the car class 
        def __init__(self, brand,model,battery_size):
            super().__init__(brand,model)
            self.battery_size=battery_size



my_car= Car("Toyata","Corola")   
print("The brand of the car is : ",my_car.brand)
print("The model of the car is :",my_car.model)
print(my_car.fullName())

my_tesla= ElectricCar("Tesla","model S","85kwh")
print(my_tesla.model( ))