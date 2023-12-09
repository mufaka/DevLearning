from shopping import load_data, get_evidence

def main():
    test_load_data()
    test_evidence()

def test_load_data():
    # no assertions here, just visually inspecting output    
    data = load_data("shopping.csv")
    print(data)

def test_evidence():
    row = ['0', '0', '0', '0', '1', '0', '0.2', '0.2', '0', '0', 'Feb', '1', '1', '1', '1', 'Returning_Visitor', 'FALSE', 'FALSE']
    expected_evidence = [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0]
    
    actual_evidence = get_evidence(row)

    assert actual_evidence == expected_evidence

if __name__ == "__main__":
    main()