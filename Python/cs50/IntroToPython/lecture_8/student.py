import random

class Student:
    def __init__(self, name, house, patronus=None):
        
        if not name:
            raise ValueError("Missing name")

        if not house:
            raise ValueError("Missing house")            

        self.name = name
        self.house = house
        self.patronus = patronus 

    def __str__(self): # same as ToString() in c#
        return f"Name: {self.name}, House: {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "STAG"
            case "Otter":
                return "OTTER"
            case "Jack Russel terrier":
                return "WOOF"
            case _:
                return "NONE"

    # properties give class designer more control; @property decorator
    
    # getter
    @property
    def house(self):
        return self._house # this cannot be same name as property

    # setter ... wtf :/
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        else:
            self._house = house  

    @property 
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        self._name = name 

    @property
    def patronus(self):
        return self._patronus 

    @patronus.setter
    def patronus(self, patronus):
        self._patronus = patronus 

    # static class variable (not self.)
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # what is the difference between @classmethod and @staticmethod?
    # guessing @staticmethod doesn't use cls and this decorator 
    # instructs python to not pass it.
    @staticmethod
    def get_random_house():
        # don't have access to houses class variable now
        return random.choice(["Gryffindor_static", "Hufflepuff_static", "Ravenclaw_static", "Slytherin_static"])


    @classmethod 
    def sort(cls): # convention
        return random.choice(cls.houses)


    @classmethod 
    def get_default(cls):
        return cls("Bill", "Gryffindor", "Stag")
