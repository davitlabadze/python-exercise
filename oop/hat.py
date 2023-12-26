import random

class Hat:

    # def __init__(self):
    #     self.houses = ["tbilis","gori","qutaisi"]

    # def sort(self,name):
    #     print(name,"is in",random.choice(self.houses))

    houses = ["tbilis","gori","qutaisi"]

    @classmethod
    def sort(cls,name):
        print(name,"is in",random.choice(cls.houses))

# hat = Hat()
# hat.sort("Harry")
        

Hat.sort("Harry")

