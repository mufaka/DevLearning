class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name 

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        if not house:
            raise ValueError("Missing house")
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        if not subject:
            raise ValueError("Missing subject")
        self.subject = subject 