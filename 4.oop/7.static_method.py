# QN> Add a static method to the class that returns a general description of a car.

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

        # kiun ki jitne baar object banega ea __init__  utni baar call hoga .
        Car.total_car +=1

    def full_name(self):
        return f"{self.brand} {self.model}" 

# static method
    @staticmethod   # also called as decorator!!
    def general_description():
        return "Cars are means of transport!" 
     


my_car= Car("Tata","Corola")
Car("Tata","Nexon")

# print(my_car.general_description())      (here object dont have permisson to access this !)


print(Car.general_description())#  static method use ho rha hai idhar .











