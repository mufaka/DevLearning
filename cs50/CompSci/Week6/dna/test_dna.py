from dna import find_match
   
def main():
    test_find_match()

"""
Run your program as python dna.py databases/small.csv sequences/1.txt. Your program should output Bob.
Run your program as python dna.py databases/small.csv sequences/2.txt. Your program should output No match.
Run your program as python dna.py databases/small.csv sequences/3.txt. Your program should output No match.
Run your program as python dna.py databases/small.csv sequences/4.txt. Your program should output Alice.
Run your program as python dna.py databases/large.csv sequences/5.txt. Your program should output Lavender.
Run your program as python dna.py databases/large.csv sequences/6.txt. Your program should output Luna.
Run your program as python dna.py databases/large.csv sequences/7.txt. Your program should output Ron.
Run your program as python dna.py databases/large.csv sequences/8.txt. Your program should output Ginny.
Run your program as python dna.py databases/large.csv sequences/9.txt. Your program should output Draco.
Run your program as python dna.py databases/large.csv sequences/10.txt. Your program should output Albus.
Run your program as python dna.py databases/large.csv sequences/11.txt. Your program should output Hermione.
Run your program as python dna.py databases/large.csv sequences/12.txt. Your program should output Lily.
Run your program as python dna.py databases/large.csv sequences/13.txt. Your program should output No match.
Run your program as python dna.py databases/large.csv sequences/14.txt. Your program should output Severus.
Run your program as python dna.py databases/large.csv sequences/15.txt. Your program should output Sirius.
Run your program as python dna.py databases/large.csv sequences/16.txt. Your program should output No match.
Run your program as python dna.py databases/large.csv sequences/17.txt. Your program should output Harry.
Run your program as python dna.py databases/large.csv sequences/18.txt. Your program should output No match.
Run your program as python dna.py databases/large.csv sequences/19.txt. Your program should output Fred.
Run your program as python dna.py databases/large.csv sequences/20.txt. Your program should output No match.    
"""    
def test_find_match():
    expected = [
        "Bob", "No match", "No match", "Alice", 
        "Lavender", "Luna", "Ron", "Ginny", 
        "Draco", "Albus", "Hermione", "Lily", 
        "No match", "Severus", "Sirius", "No match", 
        "Harry", "No match", "Fred", "No match"
    ]

    for i in range(20):
        db_file = "small" if i < 4 else "large"

        name = find_match(f"databases/{db_file}.csv", f"sequences/{i + 1}.txt")
        assert name == expected[i]


if __name__ == "__main__":
    main()