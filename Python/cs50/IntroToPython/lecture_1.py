'''
Lecture 1 - Conditionals.
https://video.cs50.io/_b6NgY_pMdw

David Malen
'''

def main():
    print("Lecture 1 - Conditionals.")
    print("https://video.cs50.io/_b6NgY_pMdw")    

    compare_1(5, 10)
    compare_1(10, 6)
    compare_1(20, 20)

    compare_2(5, 10)
    compare_2(10, 6)
    compare_2(20, 20)

    compare_3(72)
    compare_3(66)
    compare_3(104)

    compare_4(72)
    compare_4(66)
    compare_4(104)

    compare_5(72)
    compare_5(66)
    compare_5(104)

    parity_1(33)
    parity_1(26)
    parity_1(0)
    parity_1(-10)
    parity_1(-11)

    parity_2(33)
    parity_2(26)
    parity_2(0)
    parity_2(-10)
    parity_2(-11)

    match_1("Harry")
    match_1("Hermione")
    match_1("Ron")
    match_1("Draco")
    match_1("Bill")

    match_2("Harry")
    match_2("Hermione")
    match_2("Ron")
    match_2("Draco")
    match_2("Bill")

'''
>
>=
<
<=
==
!=
'''

def compare_1(x, y):
    xint = int(x)
    yint = int(y)

    if xint == yint:
        print(f"{x} and {y} are equal.")
    elif xint < yint:
        print(f"{x} is less than {y}")
    elif xint > yint:
        print(f"{x} is greater than {y}")
    else:
        print(f"Unable to determine equality for {x} and {y}")

def compare_2(x, y):
    xint = int(x)
    yint = int(y)

    if xint < yint or xint > yint:
        print(f"{x} and {y} are not equal")
    else:
        print(f"{x} and {y} are equal")

def compare_3(score):
    scoreint = int(score)

    if scoreint > 100:
        print("Grade: A+")
    elif scoreint >=90 and scoreint <= 100:
        print("Grade: A")
    elif scoreint >=80 and scoreint < 90:
        print("Grade: B")
    elif scoreint >=70 and scoreint < 80:
        print("Grade: C")
    elif scoreint >=60 and scoreint < 70:
        print("Grade: D")
    else:
        print("Grade: F")

# python lets you chain comparisons together
def compare_4(score):
    scoreint = int(score)

    if scoreint > 100:
        print("Grade: A+")
    elif 90 <= scoreint <= 100:
        print("Grade: A")
    elif 80 <= scoreint < 90:
        print("Grade: B")
    elif 70 <= scoreint < 80:
        print("Grade: C")
    elif 60 <= scoreint < 70:
        print("Grade: D")
    else:
        print("Grade: F")

def compare_5(score):
    scoreint = int(score)            

    if scoreint > 100:
        print("Grade: A+")
    elif scoreint > 90:
        print("Grade: A")
    elif scoreint > 80:
        print("Grade: B")
    elif scoreint > 70:
        print("Grade: C")
    elif scoreint > 60:
        print("Grade: D")
    else:
        print("Grade: F")


def is_even(n):
    return n % 2 == 0

def is_even_ternary(n):
    return True if n % 2 == 0 else False

def parity_1(number):
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def parity_2(number):
    if is_even_ternary(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# match is python version of switch
def match_1(name):
    match name:
        case "Harry":
            print("Gryffindor")
        case "Hermione":
            print("Gryffindor")
        case "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

def match_2(name):
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")


main()