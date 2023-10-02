'''
Lecture 0 - Functions, Variables.
https://video.cs50.io/JP7ITIXGpHk

David Malen
'''
def main():
    #hello()
    #hello_with_input()
    #hello_with_print_options()
    #hello_with_clean_str()
    #hello_with_split()
    hello_wrapping_up()

def hello():
    # print is function, "hello, world" is argument
    print("hello, world")

    '''
    functions can have side effects. print has a side
    affect of printing on screen.

    bugs - mistakes are problems for you to solve.
    print("hello, world" = SyntaxError: '(' was never closed
    '''

def hello_with_input():
    # name is variable, = is assignment operator
    name = input("What is your name? ")

    # concatenate
    #print("hello, " + name)

    # use comma - note that this will include the space
    # even though this is an argument because print
    # will automatically insert spaces as a delimiter.
    #print("hello,", name)

    # format string
    print(f"hello, {name}")

    '''
    comments, pseudocode, return values, variables.

    input expects string but you can convert that to whatever
    variable type you want
    '''

def hello_with_print_options():
    name = input("What is your dogs name? ")
    # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    print("Is it OK if I pet", end=' ')
    print(name, end='?\n')

def hello_with_clean_str():
    # remove whitespace from input with strip() (trim())
    # capitalize with capitalize() - first word
    # title() will capitalize all words
    name = input("What is your name? ").strip().title()
    print(f"hello, {name}")


def hello_with_split():
    name = input("What is your full name? ")
    # requires that the user enters two words ...
    #first, last = name.split(" ")

    # assumes at the first word is first name but doesn't suffer
    # same error result as previous when not enough input was
    # provided.
    firstName = name.split(" ")[0]

    print(f"Hello, {first}")
    print(f"Hello, {firstName}")

def hello_wrapping_up():
    name = input("What is your full name? ")
    names = name.split(" ")

    # not covered in lesson but list comprehension is pretty powerful
    print(f"Hello, {' '.join([n.strip().capitalize() for n in names if n.strip() != ''])}")


'''
Python string is str

docs.python.org is where the official documentation lives.

'''

# call the main entry for all the examples. 
# doing this way because all functions need
# to be defined before inline code is run.
main()

