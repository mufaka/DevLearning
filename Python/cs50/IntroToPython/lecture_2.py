def main():
    '''
    cat_1()
    cat_2()
    cat_3()
    cat_4()
    cat_5()
    cat_6()
    cat_7()
    cat_8()
    '''
    hogwarts_1()
    hogwarts_2()
    dict_1()
    dict_2()
    dict_3()

    mario_1()

def cat_1():
    print("meow")
    print("meow")
    print("meow")

def cat_2():
    # while
    i = 3
    while i != 0:
        print("meow")
        i -= 1

def cat_3():
    # while
    i = 0
    while i < 3:
        print("meow")
        i += 1

def cat_4():
    # for
    for i in [0, 1, 2]:
        print("for meow")

def cat_5():
    # for
    for _ in range(3):
        print(f"for range meow")

def cat_6():
    print("meow multiplier\n" * 3) #!!!!
    print("meow multiplier" * 3, end="") #!!!!

def cat_7():
    while True:
        times = int(input("What is n? "))
        if times > 0:
            break

    for _ in range(times):
        print("meow user input")

def get_number():
    while True:
        times = int(input("What is n? "))
        if times > 0:
            return times

def meow(n):
    for _ in range(n):
        print("meow")

def cat_8():
    number = get_number()
    meow(number)

def get_students():
    return ["Harry", "Hermione", "Ron", "Draco"]

def get_houses():
    return ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

def hogwarts_1():
    students = get_students()

    for name in students:
        print(name)

def hogwarts_2():
    students = get_students()

    for i in range(len(students)):
        print(i + 1, students[i])

def get_residency():
    return dict(zip(get_students(), get_houses()))

def dict_1():
    # residency = {"key": "value"}
    residency = get_residency()

    print(residency["Harry"])

def dict_2():
    residency = get_residency()

    for student in residency: # keys
        print(f"{student} lives in {residency[student]}")

def dict_3(): 
    # list of dictionaries
    students = [
        {"name": "Hermione", "house": "Gryfffindor", "patronus": "Otter" },
        {"name": "Harry", "house": "Gryfffindor", "patronus": "Stag" },
        {"name": "Ron", "house": "Gryfffindor", "patronus": "Jack Russell terrier" },
        {"name": "Draco", "house": "Slytherin", "patronus": None }
    ]

    for student in students: # keys
        print(f"{student['name']} lives in {student['house']} and their patronus is {student['patronus']}")


def print_box(height, width):
    for i in range(height): # row
        for j in range(width): # column
            print("#", end="")
        print()

def print_box_succinct(height, width):
    for i in range(height): # row
        print("#" * width)

def mario_1():
    print_box(10, 40)
    print_box_succinct(5, 20)

if __name__ == "__main__":
    main()