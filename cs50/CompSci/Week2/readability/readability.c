#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

/*
Coleman-Liau Index
index = 0.0588 * L - 0.296 * S - 15.8

L is average number of letters per 100 words
S is the average number of sentences per 100 words 

eg: "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
65 letters, 4 sentences, and 14 words
65 letters per 14 words is an average of about 464.29 letters per 100 words (because 65 / 14 * 100 = 464.29).
4 sentences per 14 words is an average of about 28.57 sentences per 100 words (because 4 / 14 * 100 = 28.57)

0.0588 * 464.29 - 0.296 * 28.57 - 15.8 = 3: Grade 3

Text: Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays 
more than any other time of year. For another, he really wanted to do his homework, but was forced to 
do it in secret, in the dead of the night. And he also happened to be a wizard.
Grade 5

Text: As the average number of letters and words per sentence increases, the Coleman-Liau index gives 
the text a higher reading level. If you were to take this paragraph, for instance, which has longer 
words and sentences than either of the prior two examples, the formula would give the text an 
twelfth-grade reading level.
Grade 12
*/

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int compute_coleman_liau(int letters, int words, int sentences);

int main(void) 
{
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    int index = compute_coleman_liau(letters, words, sentences);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int compute_coleman_liau(int letters, int words, int sentences)
{
    float l = letters / (float)words * 100;
    float s = sentences / (float)words * 100;
    float index = 0.0588 * l - 0.296 * s - 15.8;

    // roundf gets the nearst int in float format,
    // cast for caller of function.
    return (int)roundf(index);
}

int count_letters(string text)
{
    int i = 0;
    char c = text[i];
    int count = 0;

    do
    {
        if (isalpha(c))
        {
            count++;
        }

        i++;
        c = text[i];
    }
    while (c != '\0');
    
    return count;
}

int count_words(string text)
{
    int i = 0;
    char c = text[i];
    int count = 0;
    bool firstCharFound = false;

    // words are sequences of alpha characters separated by spaces,
    // but also consider start and end of string.
    do
    {
        if (c == 32) // space
        {
            if (firstCharFound)
            {
                count++;
                firstCharFound = false;
            }
        }
        else if (isalpha(c))
        {
            firstCharFound = true;
        }

        i++;
        c = text[i];

        // get the last word if we are at end of string and there are alpha
        // characters that have not been counted.
        if (c == 0 && firstCharFound)
        {
            count++;
        }
    }
    while (c != '\0');
    
    return count;
}

// naively counts sentences based on punctuation . or ! or ?. Known to be 
// incorrect with periods but solving that problem isn't in scope for this.
int count_sentences(string text)
{
    int i = 0;
    char c = text[i];
    int count = 0;
    bool firstCharFound = false;

    do
    {
        // using ascii codes instead of char literals
        if (c == 33 || c == 46 || c == 63)
        {
            count++;
        }

        i++;
        c = text[i];
    }
    while (c != '\0');
    
    return count;
}