class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        
class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        # if not name:
        #     raise ValueError("Missing name")
        # self.name = name
        self.house = house

    ...

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)

        # self.name = name
        self.house = subject

wizard = Wizard("Albus")
studnet = Student("david","tbilisi")
professor = Professor("severus","Defense agains the dark arts")