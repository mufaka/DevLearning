import argparse

balance = 0
MEOWS = 3 # not really a constant. name convention is upper

def main():
    sets()
    globals()
    constants()
    type_hints(2)
    docstrings()
    argparse_example()
    unpacking()
    args_and_kwargs()
    mapping()
    comprehensions()
    filtering()
    dictionary_comprehensions()
    enumeration()
    generators()

def sets():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"}
    ]

    # get the unique houses
    houses = set()

    for student in students:
        houses.add(student["house"])

    for house in sorted(houses):
        print(house)        

# use sparingly; frowned upon. Use class instead
def globals():
    globals_deposit(100)
    globals_withdraw(50)
    print("Balance: ", balance)


def globals_deposit(n):
    global balance 
    balance += n # UnboundLocalError without global <variable name> above ...
    
def globals_withdraw(n):
    global balance #
    balance -= n 

def constants():    
    for _ in range(MEOWS):
        print("meow")

    cat = Cat()
    cat.meow()

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


def type_hints(n: int) -> None: # <-- type hints, not enforced by python
    # like JavaScript, Python 'figures out' what type the variable is
    # pip install mypy <- checks for correct type usage
    for _ in range(n):
        print("Hello")

    # mypy doesn't recognize this as an error ...
    # type_hints("3")    

# mypy recognizes this as an error
# type_hints("3")

def docstrings():
    '''This is how you document a function'''
    '''
    This is how you document a function

    :param n: Number for somethings
    :type n: int
    :raise TypeError: If n is not an int
    :return: What it returns
    :rtype: str 
    '''
    print("Document your functions inside of the function with '''documentation here'''")

def argparse_example():
    # python lecture_notes.py -n 3
    parser = argparse.ArgumentParser(description="Describe program")
    parser.add_argument("-n", default=1, help="Number of times to print", type=int) #!!!!

    args = parser.parse_args()

    # -h, --help automatically added!!

    if args.n: # <-- not needed if default provided above
        for _ in range(int(args.n)):
            print("Argument Parser!")

def unpacking():
    # returning more than one variable
    test_string = "one,two"
    one, two = test_string.split(",")
    print(one, two)

    # list packed with values
    coins = [100, 50, 25]

    # * operator will unpack list into variables! (works with iterable)
    print(unpacking_total_knuts(*coins), "Knuts")

    coins_dict_1 = {"galleons": 100, "sickles": 50, "knuts": 25}
    coins_dict_2 = {"galleons": 100, "knuts": 25, "sickles": 50}
    coins_dict_3 = {"galleonsX": 100, "knutsX": 25, "sicklesX": 50}

    # ** operator will unpack dictionary. Note that order doesn't matter but key names do.
    print(unpacking_total_knuts(**coins_dict_1), "Knuts")
    print(unpacking_total_knuts(**coins_dict_2), "Knuts")
    # print(unpacking_total_knuts(**coins_dict_3), "Knuts") this fails because keys don't match parameter names


def unpacking_total_knuts(galleons, sickles, knuts):
    # 17 sickles per galleon, 29 knuts per sickle
    return (galleons * 17 + sickles) * 29 + knuts 


def args_and_kwargs():
    coins = [100, 50, 25]
    coins_dict_1 = {"galleons": 100, "sickles": 50, "knuts": 25}
    f(100, 50, 25)
    f(galleons = 100, sickles = 50, knuts = 25)
    f(100, 50, 25, galleons = 100, sickles = 50, knuts = 25)

    # documentation for print is print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    # implementation is print(*args, **kwargs) 


# names can be different but convention is to use args and kwargs
# * means positional list as tuple, ** means keyed list
def f(*args, **kwargs):
    print("Positional: ", args)
    print("Keyed: ", kwargs)


# map(function, list)
def mapping():
    phrases = ["hello", "hola", "aloha"]
    print(list(map(yell_1, phrases)))

    yell_2("hello", "hola", "aloha")

    lambda_map = map(lambda w: w.upper(), phrases)

    print("Lambda map")
    print(list(lambda_map))


def yell_1(phrase):
    return phrase.upper()

def yell_2(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

# [operation for variable in list if true]
# [operation for variable in list]
# [x * 2 for x in coins]
def comprehensions():
    coins = [100, 50, 75]
    doubled = [x * 2 for x in coins]
    print(doubled)

    places = [1, 2, 3, 4, 5, 6, 7, 8]
    even_doubled = [x * 2 for x in places if x % 2 == 0]
    print(even_doubled)

    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"}
    ]

    # get the Gryffindor students in a list
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]

    print(*gryffindors, sep="\n")


def filtering():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"}
    ]

    gryffindors = filter(is_gryffindor, students)

    # lamda is a anonymous function so can be used with filter or map as well
    gryffindors_2 = filter(lambda s: s["house"] == "Gryffindor", students)

    # filter returned dict because dict was passed in
    for gryffindor in sorted(gryffindors_2, key=lambda s: s["name"]):
        print(gryffindor["name"])


def is_gryffindor(student):
    return student["house"] == "Gryffindor"

def dictionary_comprehensions():
    students = [" Hermione", "Harry", "Ron"]
    gryffindors = []

    for student in students:
        gryffindors.append({"Name": student, "house": "Gryffindor"})

    print(gryffindors)

    gryffindors_2 = [{"Name": student, "house": "Gryffindor"} for student in students]

    print(gryffindors_2)

    # dictionary comprehension
    gryffindors_3 = {student: "Gryffindor" for student in students}

    print(gryffindors_3)

def enumeration():
    students = [" Hermione", "Harry", "Ron"]
    for i, student in enumerate(students):
        print(i + 1, student)

def generators():
    n = 20
    for s in sheep_yield(n):
        print(s)

# this will blow up if n is too large. it is allocating
# space for n *.
def sheep(n):
    flock = []
    for i in range(n):
        flock.append("Sheep" * i)

    return flock

# return 1 value at a time (yield)
# it returns an iterator
def sheep_yield(n):
    for i in range(n):
        yield "Sheep" * i


if __name__ == "__main__":
    main()