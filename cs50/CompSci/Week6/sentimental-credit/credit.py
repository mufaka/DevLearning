# TODO - look at solution in c from problemset 1 (luhn check)
def main():
    card_num = get_long("Number: ", 0) 

    if not is_valid_card_number(card_num):
        print("INVALID")
    else:
        print(f"{get_card_type(card_num)}")


def is_valid_card_number(card_num):
    position = 1
    last_digit = 0
    luhn_sum = 0

    # iterate the last digits in the card by dividing by 10 and taking remainder
    while card_num > 0:
        last_digit = card_num % 10

        # even numbered positions are doubled and then the sum of the 
        # result is added to the luhn sum
        if position % 2 == 0:
            doubled = last_digit * 2
            luhn_sum += int((doubled % 10)) + int((doubled / 10))
        else:
            # odd numbered digits are added to luhn sum
            luhn_sum += last_digit 

        card_num = int(card_num / 10)
        position += 1

    return luhn_sum % 10 == 0


def get_long(prompt, min):
    val = input(prompt)
    try:
        # int() converts to long
        long_val = int(val)

        if long_val < min:
            return get_long(prompt, min)
        else:
            return long_val 
        
    except:
        return get_long(prompt, min)


def get_card_type(card_num):
    # convert card_num to string so it's easier 
    # to pick off the numbers we need
    temp_str = str(card_num)
    num_count = len(temp_str)
    temp = int(temp_str[:2])

    if temp == 34 or temp == 37:
        if num_count == 15:
            return "AMEX"
    elif temp >= 51 and temp <= 55:
        if num_count == 16:
            return "MASTERCARD"
    elif temp >= 40 and temp <= 49:
        if num_count == 13 or num_count == 16:
            return "VISA"
    
    return "INVALID"


if __name__ == "__main__":
    main()