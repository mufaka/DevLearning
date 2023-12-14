import argparse
import csv


def main():
    # TODO: Check for command-line usage
    parser = argparse.ArgumentParser(
        prog="dna.py", description="Identifies a person based on DNA sequence"
    )

    parser.add_argument(
        "str_file", 
        help="The name of a CSV file containing the STR counts for a list of individuals."
    )
    parser.add_argument(
        "dna_file", 
        help="The name of a text file containing the DNA sequence to identify."
    )

    args = parser.parse_args()

    print(find_match(args.str_file, args.dna_file))

    return


# breaking this out to be testable
def find_match(str_filename, dna_filename):
    # TODO: Read database file into a variable
    """
    name,AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG
    Albus,15,49,38,5,14,44,14,12    
    """
    str_names = []
    marker_map = {}

    with open(str_filename, "r") as str_file:
        reader = csv.DictReader(str_file)
        str_names = [
            fieldname for fieldname in reader.fieldnames if fieldname != "name"
        ]

        for row in reader:
            marker_map[get_marker_key(str_names, row)] = row["name"]
            
    # TODO: Read DNA sequence file into a variable
    with open(dna_filename, "r") as dna_file:
        sequence = dna_file.readline()

    # doing this outside of with for file so it closes
    # build up key from longest sequences
    seq_vals = []
    for str in str_names:
        # TODO: Find longest match of each STR in DNA sequence
        longest = longest_match(sequence, str)
        seq_vals.append(f"{str}:{longest}")       

    lookup_key = ":".join(seq_vals)

    # TODO: Check database for matching profiles
    if lookup_key in marker_map.keys():
        return marker_map[lookup_key]
    else:
        return "No match"
    

def get_marker_key(str_names, row):
    # generate a key based on STR for 
    # a lookup of name
    # eg: 'AGATC:15:TTTTTTCT:49:AATG:38:TCTAG:5:GATA:14:TATC:44:GAAA:14:TCTG:12': 'Albus'
    vals = []
    for str in str_names:
        vals.append(f"{str}:{row[str]}")

    return ":".join(vals)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
