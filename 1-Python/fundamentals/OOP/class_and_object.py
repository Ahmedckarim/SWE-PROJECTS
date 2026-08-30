# Lesson Classes and Objects 

# In Python, classes and objects work hand in hand to organize
#    and manage data. You build a class to define shared behavior, 
#   then create objects that use those behaviors.



# E.g

class Vecicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I'm {self.make} {self.model}.")

my_car = Vecicle("Tesla", "model 3")

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()