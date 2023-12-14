from readability import count_letters, count_words, count_sentences, get_readability

def main():
    test_count_letters()
    test_count_words()
    test_count_sentences()
    test_get_readability()

def test_count_letters():
    count = count_letters("ABCDEF")
    assert count == 6

    count = count_letters("ABCDEF!@#(*&^(@#))")
    assert count == 6

    count = count_letters("A B C D E F")
    assert count == 6

    count = count_letters("A\nB\nC\nD\nE\nF")
    assert count == 6


def test_count_words():
    count = count_words("one two three")
    assert count == 3

    count = count_words("  one   two    three  ")
    assert count == 3

    count = count_words("2  one   two    three  ")    
    assert count == 3

    count = count_words("2  one   \ntwo    \tthree  ")    
    assert count == 3


def test_count_sentences():
    # TODO: we should probably treat this as a sentence, maybe assume 1
    #       as long as the length of words is greater than zero and there
    #       is no punctuation?
    count = count_sentences("This is a sentence with no punctuation")
    assert count == 0

    count = count_sentences("This is a sentence!")
    assert count == 1

    count = count_sentences("This is also a sentence.")
    assert count == 1

    count = count_sentences("Will this count as a sentence?")
    assert count == 1

    count = count_sentences("Can we count sentences? It sure would be nice if we could...")
    assert count == 2

    count = count_sentences("Congratulations! Today is your day. You're off to Great Places! You're off and away!")
    assert count == 4

    count = count_sentences("Congratulations!\nToday is your day.\tYou're off to Great Places!\nYou're off and away!")
    assert count == 4


def test_get_readability():
    readability = get_readability("One fish. Two fish. Red fish. Blue fish.") 
    assert readability == "Before Grade 1"

    readability = get_readability("Would you like them here or there? I would not like them here or there. I would not like them anywhere.") 
    assert readability == "Grade 2"

    readability = get_readability("Congratulations! Today is your day. You're off to Great Places! You're off and away!") 
    assert readability == "Grade 3"
    
    readability = get_readability("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.") 
    assert readability == "Grade 5"

    readability = get_readability("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.") 
    assert readability == "Grade 16+"


if __name__ == "__main__":
    main()