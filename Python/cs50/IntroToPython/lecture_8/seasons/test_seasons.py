import pytest
from datetime import date
from datetime import timedelta
from seasons import get_birthdate
from seasons import get_minutes_from_birthdate
from seasons import get_words_from_number

def main():
    test_invalid()
    test_valid()
    test_cs50_failed()

def test_invalid():
    with pytest.raises(ValueError):
        get_birthdate("cat")

    with pytest.raises(ValueError):
        get_birthdate("August, 30 1972")

    with pytest.raises(ValueError):
        get_birthdate("2000-02-31")

    with pytest.raises(ValueError):
        get_birthdate("8/30/1972")

def test_valid():
    # use 'yesterday' because tests can be run on any date
    today = date.today()
    yesterday = today - timedelta(1)
    assert get_minutes_from_birthdate(yesterday, today) == 1440
    assert get_words_from_number(1440) == "One thousand, four hundred forty minutes"


def test_cs50_failed():
    # Input of "1999-01-01" yields "Five hundred twenty-five thousand, six hundred minutes" when today is 2000-01-01
    birth_date = get_birthdate("1999-01-01")
    today = get_birthdate("2000-01-01")
    minutes = get_minutes_from_birthdate(birth_date, today)
    assert get_words_from_number(minutes) == "Five hundred twenty-five thousand, six hundred minutes"

    # Input of "2001-01-01" yields "One million, fifty-one thousand, two hundred minutes" when today is 2003-01-01
    birth_date = get_birthdate("2001-01-01")
    today = get_birthdate("2003-01-01")
    minutes = get_minutes_from_birthdate(birth_date, today)
    assert get_words_from_number(minutes) == "One million, fifty-one thousand, two hundred minutes"

if __name__ == "__main__":
    main()