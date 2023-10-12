import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    '''
        0-199
        200-249
        250-255
    '''
    valid_number = "([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])"

    return re.search(fr"^{valid_number}\.{valid_number}\.{valid_number}\.{valid_number}$", ip) != None

    #return re.search(r"^#\.#\.#\.#$", ip) != None

if __name__ == "__main__":
    main()