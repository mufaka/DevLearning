import re
import sys
import inflect
from datetime import date
from datetime import timedelta

def main():
    try:
        birth_date_input = input("Date of Birth: ")
        birth_date = get_birthdate(birth_date_input)
        today = date.today()

        minutes_from_birth = get_minutes_from_birthdate(birth_date, today)
        words = get_words_from_number(minutes_from_birth)
        print(words)
    except ValueError:
        sys.exit("Invalid date")
    #except:
     #   sys.exit("Unknown error")

def get_birthdate(birth_date_input):
    date_re = r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$"

    if matches := re.search(date_re, birth_date_input):
        return date.fromisoformat(birth_date_input)
    else:
        raise ValueError("Invalid ISO date provided")

def get_minutes_from_birthdate(birth_date, today):
    days_from_birth_delta = today - birth_date
    minute_delta = timedelta(minutes = 1)
    # operator overload returns float, but want int for inflect
    return int(days_from_birth_delta / minute_delta)

def get_words_from_number(n):
    # only using the engine once, so instantiating here is OK
    inflect_engine = inflect.engine()
    words = inflect_engine.number_to_words(n).replace(" and", "").capitalize()
    return words + " minutes"

if __name__ == "__main__":
    main()