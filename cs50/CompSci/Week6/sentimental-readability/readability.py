from cs50 import get_string


# TODO - look at solution in c from problemset 2 (Coleman-Liau Index)
def main():
    text = get_string("Text: ")
    print(get_readability(text))


def get_readability(text):
    index = compute_coleman_liau(
        count_letters(text), count_words(text), count_sentences(text)
    )
    
    # print(f"Index {index} for {text}")

    if index < 1:
        return "Before Grade 1"
    elif index >= 16:
        return "Grade 16+"
    else:
        return "Grade " + str(index)
    

def count_letters(text):
    count = 0

    # count all alpha characters
    for c in text:
        if c.isalpha():
            count += 1

    return count


def count_words(text):
    count = 0

    # splits on whitespace
    words = text.split()

    # check to see if word has an alpha count > 0
    # this considers numbers as not words
    for word in words:
        if count_letters(word) > 0:
            count = count + 1

    return count


def count_sentences(text):
    count = 0

    words = text.split()

    # words is list from the text separated by 
    # whitespace (' ', '\t', '\n' etc). If a word
    # ends with a punctuation character '.', '?', or '!'
    # then assume it marks a sentence
    sentence_chars = [".", "?", "!"]

    for word in words:
        if word[-1] in sentence_chars:
            count += 1

    return count 


def compute_coleman_liau(letters, words, sentences):
    # Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, 
    # where L is the average number of letters per 100 words in the text, and S is the 
    # average number of sentences per 100 words in the text.
    l = letters / float(words) * 100
    s = sentences / float(words) * 100
    index = 0.0588 * l - 0.296 * s - 15.8

    return int(round(index))


if __name__ == "__main__":
    main()