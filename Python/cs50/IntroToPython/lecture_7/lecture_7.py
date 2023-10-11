import re

def main():
    #validate_1()
    #validate_2()
    validate_3()

def validate_1():
    email = input("Email address? ").strip()

    username, domain = email.split("@")

    # with an @ - still not good enough. can keep going
    if username and "." in domain:
        print("Valid")
    else:
        print("Invalid")

def validate_2():
    email = input("Email address? ").strip()

    '''
        re.search(pattern, string, flags=0)

        flags:
        re.IGNORECASE
        re.MULTILINE
        re.DOTALL -> dot recognizes newline as well

        .           any char except newline
        *           0 or more repetitions
        +           1 or more repetitions
        ?           0 or 1 repetition
        {m}         m repetitions
        {m-n}       m-n repetitions
        ^           matches the start of the string
        $           matches the end of the string or just before the newline at the end of the string
        []          set of characters - one or more characters that belong
        [^]         complementing the set - one or more characters that don't belong
        \w          word - alphanumeric or underscore
        \W          not word
        \d          decimal digit
        \D          not a decimal digit
        \s          whitespace character
        \S          not whitespace character
        A|B         either A or B
        (...)       a group <-- captured as a return
        (?:...)     non-capturing version


        := walrus operator
    '''

    # r"raw text" means leave escape characters alone. 
    # re.fullmatch adds ^ and $ for you
    if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|gov|net|ai|com|org)$", email):
        print("Valid")
    else:
        print("Invalid")

def validate_3():
    name = input("What is your name? ").strip()
    matches = re.search(r"^(.+), (.+)$", name)

    if matches:
        last, first = matches.groups()
        # last = matches.groups(1)
        # first = matches.groups(2)
        # name = f"{matches.groups(2)} {matches.groups(1)}"
        name = f"{first} {last}"

    '''
        if matches := re.search(r"^(.+), (.+)$", name):
            name = f"{matches.groups(2)} {matches.groups(1)}"
    '''

    print(f"{name}")

def substitution_1():
    # re.sub(pattern, repl, string, count, flags)


if __name__ == "__main__":
    main()