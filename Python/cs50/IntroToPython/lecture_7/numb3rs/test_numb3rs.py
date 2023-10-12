from numb3rs import validate

def main():
    test_valid()
    test_invald()

def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("10.0.0.0") == True
    assert validate("0.10.0.0") == True
    assert validate("0.0.10.0") == True
    assert validate("0.0.0.10") == True
    assert validate("99.0.0.0") == True
    assert validate("0.99.0.0") == True
    assert validate("0.0.99.0") == True
    assert validate("0.0.0.99") == True
    assert validate("100.0.0.0") == True
    assert validate("0.100.0.0") == True
    assert validate("0.0.100.0") == True
    assert validate("0.0.0.100") == True
    assert validate("10.0.0.0") == True
    assert validate("0.10.0.0") == True
    assert validate("0.0.10.0") == True
    assert validate("0.0.0.10") == True
    assert validate("255.255.255.255") == True
    

def test_invalid(): 
    assert validate("") == False
    assert validate("cat") == False
    assert validate("cat.dog.rabbit.lizard") == False
    assert validate("1.2.3") == False
    assert validate("...") == False
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("1.1.1.1.1") == False


if __name__ == "__main__":
    main()