# TODO
def main():
    height = get_int("Height: ", 1, 8)

    # first half of line is space padded to height size
    # second half of line is # * row
    for i in range(height):
        row = i + 1
        print(" " * (height - row), end="")
        print("#" * row, end="  ")
        print("#" * row)


def get_int(prompt, min, max):
    val = input(prompt)
    try:
        int_val = int(val)

        if int_val < min or int_val > max:
            return get_int(prompt, min, max)
        else:
            return int_val 
        
    except:
        return get_int(prompt, min, max)


if __name__ == "__main__":
    main() 