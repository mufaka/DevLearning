import csv
from cs50 import SQL

def main():
    """
    SQL

    Starts with csv and some overlap of the Intro To Python course

    Much of the SQL I've had experience with so jumping into problem sets
    to learn the nuances of sqlite and working with it in python.
    """
    # favorites_1()
    # favorites_2()
    favorites_3()
    sql_1()
    sql_2()
    imdb_1()


def favorites_1():
    with open("src7/favorites/favorites.csv") as file:
        reader = csv.reader(file)

        # skip the header row
        next(reader)

        for row in reader:
            print(row[1])

def favorites_2():
    with open("src7/favorites/favorites.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row["language"])

# keep track of counts in a dictionary
counts = {}

def favorites_3():
    with open("src7/favorites/favorites.csv") as file:
        reader = csv.DictReader(file)


        for row in reader:
            language = row["language"]

            if language in counts:
                counts[language] += 1
            else:
                counts[language] = 1

    # this is pretty cool.
    #for language in sorted(counts, key=get_value, reverse=True):
    #    print(f"{language}: {counts[language]}")
    for favorite in sorted(counts, key=lambda favorite: counts[favorite], reverse=True):
        print(f"{favorite}: {counts[favorite]}")


def get_value(language):
    return counts[language]


def sql_1():
    db = SQL("sqlite:///src7/favorites/favorites.db")
    rows = db.execute("SELECT * FROM favorites")

    for row in rows:
        print(row["language"])

def sql_2():        
    db = SQL("sqlite:///src7/favorites/favorites.db")
    rows = db.execute("SELECT COUNT(*) , language FROM favorites GROUP BY language ORDER BY COUNT(*) desc")

    for row in rows:
        print(row["language"], row["COUNT(*)"])



if __name__ == "__main__":
    main()