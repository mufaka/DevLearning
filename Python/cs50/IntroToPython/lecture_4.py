'''
module is library with one or more features in it
'''
import sys
import random
import statistics

def main():
    for i in range(2):
        module_1()
        module_2()
    
    module_3()
    module_4()
    module_5()
    module_6()

def module_1():
    # random.py
    pick = random.choice(range(10))
    print(pick)


def module_2():
    pick = random.randint(1, 10)
    print(pick)


def module_3():
    faces = ["Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two"]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    deck = []

    for suit in suits:
        for face in faces:
            deck.append(f"{face} of {suit}")
    
    #shuffle(deck) this doesn't seem to be very good at shuffling

    shuffled_deck = []

    while len(deck) > 0:
        random_card = random.choice(deck)
        shuffled_deck.append(random_card)
        deck.remove(random_card)

    print(shuffled_deck)

def module_4():
    print(statistics.mean([82, 92, 77, 95, 44]))

def module_5():
    for arg in sys.argv[1:]:
        print(arg)

    # arg[0] is the file name running

def module_6():
    if len(sys.argv) < 2:
        sys.exit("You must provide a name on the command line.")

    print("Hello", sys.argv[1])

def packages_1():
    # packages used for third party library
    # a module implemented in a folder
    # PyPi (pypi.org)
    print("Visit pypi.org")

def requests_1():
    # package is requests
    print("Use the requests package to send http requests")


main()