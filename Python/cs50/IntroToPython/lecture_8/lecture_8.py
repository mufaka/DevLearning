from student import Student 

def main():
    student_1()

def student_1():
    #name = get_name()
    #house = get_house()
    student = get_student_class()

    print(f"{student.name} from {student.house}")
    print(student)
    print(student.charm())

    print(Student.sort())

    print(Student.get_default())
    print(Student.get_random_house())


def get_input_str(prompt):
    return input(prompt)

def get_name():
    return input()

def get_house():
    return input()

def get_student():
    return {
        "Name": get_name(),
        "House": get_house()
    }

def get_student_props():
    return get_name(), get_house()

def get_student_class():
    # what kind of wackiness is this?
    # the class definition doesn't have 
    # name or house properties ... it's
    # like javascript prototypes where you
    # can just randomly add whatever you 
    # want ... maybe there is some way to
    # prevent this and force a strict model?
    name = get_input_str("Name: ")
    house = get_input_str("House: ")
    patronus = get_input_str("Patronus: ")

    return Student(name, house, patronus)

if __name__ == "__main__":
    main()