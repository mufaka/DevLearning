import csv 

def main():
    names()
    read_csv()
    read_csv_dict("names_dict.csv")
    write_csv_file()
    # https://pillow.readthedocs.io/en/stable/ (PIL, Python Image Library)

def names():
    names = []

    for i in range(4):
        name = input(f"Name {i + 1}: ")
        names.append(name)

    names.sort()

    with open("names.txt", "w") as file:
        for i in range(len(names)):
            file.write(f"{names[i]}\n")

    read_file_1("names.txt")
    read_file_2("names.txt")


def read_file_1(filename):
    with open(filename, "r") as read_file:
        # readlines will include newline character :(
        lines = read_file.readlines()

        for line in lines:
            print(line.rstrip())

        # shortcut is to just 'for line in read_file'

def read_file_2(filename):
    names = []

    with open(filename, "r") as read_file:
        for line in read_file:
            names.append(line.rstrip())

    for name in sorted(names, reverse = True):
        print(name)

def read_csv():
    names = []

    with open("names.csv", "r") as csv_file:
        reader = csv.reader(csv_file)

        for name, age in reader:
            names.append({"name": name, "age": age})

    for person in sorted(names, key=lambda x: x["age"]):
        print(f"{person['name']} is {person['age']} years old")

def read_csv_dict(filename):
    names = []

    with open(filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            names.append({"Name": row['Name'], "Age": row['Age']})

    for person in sorted(names, key=lambda x: x["Age"], reverse=True):
        print(f"{person['Name']} is {person['Age']} years old")


def write_csv_file():
    with open("names_dict_2.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age"])
        writer.writeheader()
        writer.writerow({"Name": 'Bill', "Age": 51})
        writer.writerow({"Name": 'Tanner', "Age": 15})
        writer.writerow({"Name": 'Blaise', "Age": 11})
        writer.writerow({"Name": 'Michelle', "Age": 47})


    read_csv_dict("names_dict_2.csv")


if __name__ == "__main__":
    main()