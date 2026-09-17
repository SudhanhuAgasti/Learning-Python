# QN>  Use a property decorator in the car class to make the model attributes read-only.

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand= brand

        # make it read only using decorator
        # st-1 >  make it private 1st useing underscore
        self.__model= model

    @property  # use generally when we not to change any property opeartor
    def model(self):
        return self.__model    



     


my_car= Car("Tata","Safari")

# my_car.model="city" # overrite the model of the car.



# print("The model of the car is : ",my_car.model())
print("The model of the car is : ",my_car.model)
