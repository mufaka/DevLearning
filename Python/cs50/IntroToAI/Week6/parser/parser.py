import nltk
from nltk.tokenize import word_tokenize
import sys
import os

# nltk.download('punkt')

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP
NP -> N | Det N | Det Adj NP | NP NP | P NP | Adj NP | N Adj | NP Adv
VP -> V | V NP | VP Conj VP | NP VP | Adv VP | VP Adv
"""

"""
This is generated from the map_terminals function below
1 -  (N)holmes (V)sat 
2 -  (N)holmes (V)lit (Det)a (N)pipe 
3 -  (N)we (V)arrived (Det)the (N)day (P)before (N)thursday 
4 -  (N)holmes (V)sat (P)in (Det)the (Adj)red (N)armchair (Conj)and (N)he (V)chuckled 
5 -  (Det)my (N)companion (V)smiled (Det)an (Adj)enigmatical (N)smile 
6 -  (N)holmes (V)chuckled (P)to (N)himself 
7 -  (N)she (Adv)never (V)said (Det)a (N)word (Conj)until (N)we (V)were (P)at (Det)the (N)door (Adv)here 
8 -  (N)holmes (V)sat (Adv)down (Conj)and (V)lit (Det)his (N)pipe 
9 -  (N)i (V)had (Det)a (Adj)country (N)walk (P)on (N)thursday (Conj)and (V)came (N)home (P)in (Det)a (Adj)dreadful (N)mess 
10 - (N)i (V)had (Det)a (Adj)little (Adj)moist (Adj)red (N)paint (P)in (Det)the (N)palm (P)of (Det)my (N)hand 

Extracting POS tags from above and sorting:
Det N V Det Adj N
N Adv V Det N Conj N V P Det N Adv
N V 
N V Det N
N V Det N P N
N V P Det Adj N Conj N V
N V P N
N V Adv Conj V Det N <-- two sentences NP Conj VP
N V Det Adj N P N Conj V N P Det Adj N
N V Det Adj Adj Adj N P Det N P Det

The trick now is to nest these as succinctly as possible

S -> NP VP 
NP -> N | Det N | Det Adj NP | P NP
VP -> V | V NP | Adv VP

This is a good base, update above as sentences fail.

"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # map_terminals()
    # test_parsing()
    # sys.exit(0)

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    print(s)
    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    words = []
    tokenized = word_tokenize(sentence)

    for token in tokenized:
        if token.isalpha():
            words.append(token.lower())

    return words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    nps = []

    # you can filter the subtrees
    for subtree in tree.subtrees(lambda s: s.label() == "NP"):
        # are there any subtrees of the subtree labeled NP?
        count = 0
        for _ in subtree.subtrees(lambda s: s.label() == "NP"):
            count += 1

        if count == 1:
            nps.append(subtree)
    
    return nps 


# the sentences we have are examples for which to build
# a context free grammar. POS tagging has been done for us 
# with the terminals, so use them for determining the example
# sentence structures.
def map_terminals():
    map = get_terminal_map()

    for i in range(10):
        filename = f"sentences{os.path.sep}{i + 1}.txt"
        with open(filename) as f:
            s = f.read()
            words = preprocess(s)

            for word in words:
                print(f"({map[word]}){word}", end=" ")

            print()


def get_terminal_map():
    map = {}

    lines = TERMINALS.splitlines()

    for line in lines:
        if len(line.strip()) > 0:
            tokens = line.split("|")

            # First token has POS and first word: Adj -> "country"
            pos_tokens = tokens[0].split("->")
            pos_token = pos_tokens[0].strip()
            first_word = pos_tokens[1].replace('"', "").strip()

            map[first_word] = pos_token

            for i, v in enumerate(tokens):
                if i > 0:
                    word = v.replace('"', "").strip()
                    map[word] = pos_token 

    return map


def test_parsing():
    for i in range(10):
        filename = f"sentences{os.path.sep}{i + 1}.txt"
        with open(filename) as f:
            s = f.read()
            words = preprocess(s)

            try:
                trees = list(parser.parse(words))
            except ValueError as e:
                print(e)
                return
            if not trees:
                print(f"Could not parse {filename}.")
                print(s)


if __name__ == "__main__":
    main()
