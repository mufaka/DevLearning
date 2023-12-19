import nltk
import cs50

def main():
    nltk_1()
    nltk_2()
    nltk_3()

    """
    Natural Language Processing (NLP)

        Automatic Summarization
        Information Extraction
        Language Identification
        Machine Translation
        Named Entity Recognition (NER)
        Speech Recognition
        Text Classification
        Word Sense Disambiguation
            - AI chooses right meaning of a word that has multiple meanings
            - eg: banks means both financial institution and ground on sides of rivers

    Syntax - sentence structure
        Can be grammatically correct but ambiguous at the same time
            eg: "I saw the man with the telescope"
                - did you see "the man" by looking through the telescope or
                - did you see "the man" that had a telescope?

    Semantics - sentence meaning
        "Just before nine o'clock Sherlock Holmes stepped briskly into the room"
        "Sherlock Holmes stepped briskly into the room just before nine o'clock"
        "A few minutes before nine, Sherlock Holmes walked quickly into the room"

            - all have same meaning

        A sentence can also be grammatically correct but have nonsensical meaning:
            "Colorless green ideas sleep furiously"


    Context-Free Grammar

        Formal Grammer
            - set of rules for generating sentences in a language.

        Context-Free
            - text abstracted from meaning to represent the structure

                - She saw the city. <- each word is a terminal word; once generated it is done.

                    She and city are nouns (N)
                    Saw is a verb (V)
                    the is the determiner (D); can be definite or indefinite

                    N   V   D   N
                    She Saw The City

                    Non terminal symbols are replaced with terminal words
                    N - she | city | car | Harry | ...
                    D - the | a | an | ...
                    V - saw | ate | waled | ...
                    P - to | on | over | ...
                    ADJ - blue | busy | old | ...

                    Non-Terminal Symbols can also be replaced by Non-Terminal Symbols
                    NP (Noun Phrase) - N | D N (Noun or Determiner and Noun)
                    VB (Verb Phrase) - VP | V NP
                    S (Sentence) - NP VP

                    Noun Phrase (NP) is a group of works that connect to a noun. 

                        She
                        The City

                    Verb Phrase (VP) is a group of words that connect to the verb

                        Saw, saw the city

                            S              
                    _______|___            
                    |           VP         
                    |    _______|___        
                    NP  |           NP     
                    |   |        ___|___    
                    N   V       D       N  
                    |   |       |       |   
                    she saw     the     city

        nltk (Natural Language Toolkit)

        see nltk_1() and nltk_2()

        NOTE: creating the grammars is difficult

        n-gramn
            a contiguous sequence of n items from a sample of text (n can be characters or words)

            "How often have I said to you that when you have eliminated the impossible whatever remains,
            however improbable, must be the truth?"

                tri-grams: 
                    How often have
                    often have I
                    have I said
                    etc.

            Look at ngrams.py

                # corpus is a body, or bodies of, text.
                ngrams = Counter(nltk.ngrams(corpus, n))

                # ngrams is a Counter, Counter has most_common function
                for ngram, freq in ngrams.most_common(10):
                    print(f"{freq}: {ngram}")

            tokenization
                the task of splitting a sequence of characters into pieces (tokens)

            You can build a Markov Chain from the common ngrams
                - can be used to predict next word in sequence.

                Look at generator.py for an example

                text_model = markovify.Text(text)

                # Generate sentences
                print()
                for i in range(5):
                    print(text_model.make_sentence())
                    print()
                
                # NOTE: the generated text probably doesn't make sense


            Text Classification

                Good Email or Spam

                Sentiment analysis - Positive or Negative

                bag-of-words model
                    model that represents text as an unordered collection of words

                    NOTE: loses information, order of words matters (also context)

                Naive Bayes
                    Classify Text based on Bayes' Rule

                    P(b|a) = P(a|b) P(b)
                            ------------
                                P(a)

                    Probability of b given a is probability of a given b multiplied by probability of b divided by the probability of a

                    P(Positive)

                    P(Negative)

                        "My grandson loved it!"

                        P(positive | "My grandson loved it!")
                        
                        P(positive | "my", "grandson", "loved", "it") <-- unordered collection of words.

                        P("my", "grandson", "loved", "it" | positive)P(positive)
                        --------------------------------------------------------
                                P("my", "grandson", "loved", "it") <-- not needed

                        
                        P(positive | "my", "grandson", "loved", "it")

                            proportional to

                        P("my", "grandson", "loved", "it" | positive)P(positive)

                        = a joint probability of all being the case
                        P(positive, "my", "grandson", "loved", "it")

                        Naive - assume all words are independent of each other. Only depends on positive or negative

                        P(positive | "my", "grandson", "loved", "it")

                            naively proportional to

                            P(positive)P("my", positive)P("grandson", positive) etc


                        If we have training data:

                        P(positive) = number of positive samples
                                     ---------------------------
                                        number of total samples

                        P("loved") = number of positive samples with "loved"
                                     ---------------------------------------
                                        number of positive samples

                        

                        Example: (see lecture notes for better visual)

                        Positive  Negative              Positive    Negative
                        0.49      0.51            my     0.30        0.20
                                            grandson     0.01        0.02
                                               loved     0.32        0.08
                                                  it     0.30        0.40

                        P(positive)P("my", positive)P("grandson", positive) etc

                        NOTE: problem if, for example, grandson doesn't appear in positive samples. We'll calculate zero


                        Additive Smoothing
                            Add a value, alpha, to each value in our distribution to smooth the data

                            Laplace Smoothing
                                Add 1 to each value in our distribution:
                                    pretending we've seen each value one more time than actual


                        Look at sentiment.py


                    Word Representation - vectors

                        NN takes numbers as input

                        One-Hot
                            he      1 0 0 0
                            wrote   0 1 0 0
                            a       0 0 1 0
                            book    0 0 0 1

                            Gets too big too fast.
                            Can't "group" words by meaning, no way to determine distance between them

                        Distributed Representation

                            representation of meaining distributed across multiple values

                            "He wrote a book"

                            he      -0.34, -0.08, 0.02, -0.18 ....
                            wrote   ...
                            a       ...
                            book    ...

                            Ideally, similiar words have a similiar vector representation.

                            "You should know a word by the company it keeps." - J.R. Firth, 1957

                                Define the meaning of a word by the words around it; the context. 

                                for _____ he ate.
                                    breakfast, lunch, dinner, snack (meal names)


                                word2vec model for generating word vectors

                                    -- look at vectors.py


                                word2vec can capture the relationships between words

                                king - man = x (distance between vector representations)
                                woman + x = queen (similar distance)

                                
                    Word Vectors can be passed into neural network.
                        - machine translation (english to french) 
                            - translating a sequence

                        need fixed size for NN input

                        
                        Recurrent Neural Networks
                            hidden state passed to subsequent runs of NN

                            Encoder Decoder architecture

                            What -> NN 
                                    - hidden state
                            is   -> NN
                                    - hidden state

                                    hidden state passed in as well

                            the capital of Massachusetts passed in as well, hidden state updated along the way.

                            <end> token -> NN -> The
                            The -> NN -> capital
                            capital -> NN -> is
                            is -> NN -> Boston

                            Boston -> NN -> <end>
                                

                            Look at lecture notes for better visual. A sequence goes into the encoder and generates final hidden state. Then 
                            the decoding process starts.

                        Used to be the best way to do this but has problems
                            encoder stage -> final hidden state needs all information from the sequence. Large sequences make it difficult / expensive.
                            hidden state weight / importance vary
                            each run of the network is dependent on previous run.


                        Attention
                            which values are important to pay attention to when generating a sequence

                            What is the capital of Massachusetts

                                the capital is _____ <- capital and Massachusetts are the most important words at this point

                                Attention scores for each word

                                Look at lecture notes for this.

                                We have hidden state for each word and now attention scores for each word. The dot product of those
                                gives us a context vector value that can be fed into the decoder.
                        
                            NOTE: without Attention, there is no way to give weight to each hidden state and they would all be treated equally.
                                  Attention gives you a means to weight the words to narrow down a context vector. 

                            First used for translation. 

                        Transformers
                            allows for parallel processing. better performance and quicker training

                            Encoding
                                independent processing
                                    input word + positional encoding -> Self-Attention -> NN -> encoded representation

                                    Keep track of order separately so you don't have to run in sequence.
                                        - positional encoding + input word is the vector input
                                        - multiple self-attention layers allow for handling multiple facets of the input at the same time

                                    Self-Attention -> NN can also be run multiple times to learn deeper patterns

                            Decoding

                                previous output word + positional encoding -> Self-Attention -> Attention -> NN -> next output word


    Course Recap - just scratched the surface:
    Search
    Knowledge
    Uncertainty
    Optimization
    Learning
    Neural Networks
    Language
                            

    """

def nltk_1():
    grammar = nltk.CFG.fromstring("""
        S -> NP VP

        NP -> D N | N
        VP -> V | V NP

        D -> "the" | "a"
        N -> "she" | "city" | "car"
        V -> "saw" | "walked"
    """)

    parser = nltk.ChartParser(grammar)    

    sentence = "she saw the city".split() # input("Sentence: ").split()
    try:
        for tree in parser.parse(sentence):
            tree.pretty_print()
            # tree.draw() - tk not working on WSL
    except ValueError:
        print("No parse tree possible.")


def nltk_2():
    # AP = Adjective Phrase
    # PP = Prepsositional Phrase
    grammar = nltk.CFG.fromstring("""
        S -> NP VP

        AP -> A | A AP
        NP -> N | D NP | AP NP | N PP
        PP -> P NP
        VP -> V | V NP | V NP PP

        A -> "big" | "blue" | "small" | "dry" | "wide"
        D -> "the" | "a" | "an"
        N -> "she" | "city" | "car" | "street" | "dog" | "binoculars"
        P -> "on" | "over" | "before" | "below" | "with"
        V -> "saw" | "walked"
    """)

    parser = nltk.ChartParser(grammar)

    #sentence = "she saw the wide street".split() #input("Sentence: ").split()
    # NOTE: There are two separate parse trees for the following:
    sentence = "she saw the dog with the binoculars".split() 

    # First has PP modifying 'saw" => she saw with the binoculars

    try:
        for tree in parser.parse(sentence):
            tree.pretty_print()
    except ValueError:
        print("No parse tree possible.")    


def nltk_3():
    grammar = nltk.CFG.fromstring("""
        S -> NP V

        NP -> N | A NP

        A -> "small" | "white"
        N -> "cats" | "trees"
        V -> "climb" | "run"
    """)

    parser = nltk.ChartParser(grammar)

    sentence1 = "cats run".split() 
    sentence2 = "cats climb trees".split() 
    sentence3 = "small cats run".split() 
    sentence4 = "small white cats climb".split() 

    try:
        for tree in parser.parse(sentence1):
            tree.pretty_print()
    except ValueError:
        print("No parse tree possible.")    

    try:
        for tree in parser.parse(sentence2):
            tree.pretty_print()
    except ValueError:
        print("No parse tree possible.")    

    try:
        for tree in parser.parse(sentence3):
            tree.pretty_print()
    except ValueError:
        print("No parse tree possible.")    

    try:
        for tree in parser.parse(sentence4):
            tree.pretty_print()
    except ValueError:
        print("No parse tree possible.")    


if __name__ == "__main__":
    main()