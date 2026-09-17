# QN>  Create two classes battery and enginee and let the electricar class inherit from the both,demonstrating multiple inheritence

class Car: 
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

class Battery:
    def battery_info(self):
        return "This is battery."

class Enginee:
    def enginee_info(self):
        return "This is enginee."


class ElectricCar(Battery,Enginee,Car):
    pass


my_tesla=  ElectricCar("Tesla","Model s")   
print(my_tesla.enginee_info()) 
print(my_tesla.battery_info()) 

