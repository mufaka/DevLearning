def main():
    exceptions_1()
    exceptions_2()
    exceptions_3()
    exceptions_4()
    exceptions_5()
    exceptions_6()

def exceptions_1():
    # enter an alpha character to break
    x = int(input("Enter a number: "))
    print(f"x is {x}")

def exceptions_2():
    try:
        x = int(input("Enter a number: "))
        print(f"x is {x}")

    except ValueError:
        print("Only numbers are allowed")
        exceptions_2()
    except:
        print("Something horrible happened")

def exceptions_3():
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Only numbers are allowed")
    else:
        # else is for the exception, so no 
        # exception happened
        print(f"x is {x}")
    
    # note the x will not be assigned/available
    # if the int cast fails ... so this code 
    # shouldn't be here
    #print(f"x is {x}")

def exceptions_4():
    while True:    
        try:
            x = int(input("Enter a number: "))
            break
        except ValueError:
            print("Only numbers are allowed")

    print(f"x is {x}")


def get_int():
    while True:    
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Only numbers are allowed")

def get_int_pass():
    while True:    
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass


def exceptions_5():    
    x = get_int()
    print(f"Function returned {x}")

def exceptions_6():
    # pass - used to not do anything for the exception
    x = get_int_pass()
    print(f"Function returned {x}")


main()