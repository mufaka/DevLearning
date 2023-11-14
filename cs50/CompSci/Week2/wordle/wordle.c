#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

// each of our text files contains 1000 words
#define LISTSIZE 1000

// values for colors and score (EXACT == right letter, right place; CLOSE == right letter, wrong place; WRONG == wrong letter)
#define EXACT 2
#define CLOSE 1
#define WRONG 0

// ANSI color codes for boxed in letters
#define GREEN   "\e[38;2;255;255;255;1m\e[48;2;106;170;100;1m"
#define YELLOW  "\e[38;2;255;255;255;1m\e[48;2;201;180;88;1m"
#define RED     "\e[38;2;255;255;255;1m\e[48;2;220;20;60;1m"
#define RESET   "\e[0;39m"

// user-defined function prototypes
string get_guess(int wordsize);
int check_word(string guess, int wordsize, int status[], string choice);
void print_word(string guess, int wordsize, int status[]);
bool isnumber(string arg);
int count_letters(string text);

int main(int argc, string argv[])
{
    // ensure proper usage
    // TODO #1
    if (argc != 2) 
    {
        printf("Usage: ./wordle wordsize\n");
        return 1; // 1 means incorrect argument count
    }
    else 
    {

        // we have one argument, is it a numeric?
        if (!isnumber(argv[1]))
        {
            printf("Usage: wordsize must be either 5, 6, 7, or 8\n");
            return 2; // 2 means non-numeric, or negative number, argument provided for wordsize
        }

        // is the argument string length 1?
        if (strlen(argv[1]) != 1) 
        {
            printf("Usage: wordsize must be either 5, 6, 7, or 8\n");
            return 3; // 3 means numeric argument to big
        }

        // we have a 1 digit (numeric) argument
    }

    int wordsize = 0;

    // ensure argv[1] is either 5, 6, 7, or 8 and store that value in wordsize instead
    // TODO #2
    wordsize = argv[1][0] - '0'; // found this as a standard way to convert 0-9 as chars to 0-9 as ints

    if (wordsize < 5 || wordsize > 8)
    {
        printf("Usage: wordsize must be either 5, 6, 7, or 8\n");
        return 1; // 4 means numeric argument isn't in range; NOTE: had to change to 1 because check50 expects 1 for some reason.
    }

    // open correct file, each file has exactly LISTSIZE words
    char wl_filename[6];
    sprintf(wl_filename, "%i.txt", wordsize);
    FILE *wordlist = fopen(wl_filename, "r");
    if (wordlist == NULL)
    {
        printf("Error opening file %s.\n", wl_filename);
        return 1;
    }

    // load word file into an array of size LISTSIZE
    char options[LISTSIZE][wordsize + 1];

    for (int i = 0; i < LISTSIZE; i++)
    {
        fscanf(wordlist, "%s", options[i]);
    }

    // pseudorandomly select a word for this game
    srand(time(NULL));
    string choice = options[rand() % LISTSIZE];

    // allow one more guess than the length of the word
    int guesses = wordsize + 1;
    bool won = false;

    // print greeting, using ANSI color codes to demonstrate
    printf(GREEN"This is WORDLE50"RESET"\n");
    printf("You have %i tries to guess the %i-letter word I'm thinking of\n", guesses, wordsize);

    // main game loop, one iteration for each guess
    for (int i = 0; i < guesses; i++)
    {
        // obtain user's guess
        string guess = get_guess(wordsize);

        // array to hold guess status, initially set to zero
        int status[wordsize];

        // set all elements of status array initially to 0, aka WRONG
        // TODO #4
        memset(status, 0, sizeof status);

        // Calculate score for the guess
        int score = check_word(guess, wordsize, status, choice);

        printf("Guess %i: ", i + 1);
        
        // Print the guess
        print_word(guess, wordsize, status);

        // if they guessed it exactly right, set terminate loop
        if (score == EXACT * wordsize)
        {
            won = true;
            break;
        }
    }

    // Print the game's result
    // TODO #7
    if (won)
    {
        printf("You won!\n");
    }
    else
    {
        printf("%s\n", choice);
    }

    // that's all folks!
    return 0;
}

string get_guess(int wordsize)
{
    string guess = "";

    // ensure users actually provide a guess that is the correct length
    // TODO #3
    do
    {
        guess = get_string("Input a %i-letter word: ", wordsize);
    } 
    while (count_letters(guess) != wordsize);

    return guess;
}

int check_word(string guess, int wordsize, int status[], string choice)
{
    int score = 0;

    // compare guess to choice and score points as appropriate, storing points in status
    // TODO #5
    // iterate over each letter of the guess
    for (int i = 0; i < wordsize; i++)
    {
        char g = toupper(guess[i]);

        // iterate over each letter of the choice
        for (int j = 0; j < wordsize; j++)
        {
            char c = toupper(choice[j]);

            // compare the current guess letter to the current choice letter
            if (g == c) 
            {
                // if they're the same position in the word, score EXACT points (green) and 
                //break so you don't compare that letter further
                if (i == j)
                {
                    status[i] = EXACT;
                    // keep track of the total score by adding each individual letter's score from above
                    score += EXACT;
                } // if it's in the word, but not the right spot, score CLOSE point (yellow)
                else
                {
                    // motion
                    // second correct guess of o will mark first one as close even if it is marked exact already
                    // need to check if it's not currently marked exact.

                    if (status[i] != EXACT)
                    {
                        status[i] = CLOSE;
                        // keep track of the total score by adding each individual letter's score from above
                        score += CLOSE;
                    }
                }
            }
        }
    }

    return score;
}

void print_word(string guess, int wordsize, int status[])
{
    // print word character-for-character with correct color coding, then reset terminal font to normal
    // TODO #6
    for (int i = 0; i < wordsize; i++)
    {
        if (status[i] == 2) 
        {
            printf(GREEN"%c",guess[i]);
        }
        else if (status[i] == 1)
        {
            printf(YELLOW"%c",guess[i]);
        }
        else
        {
            printf(RED"%c",guess[i]);
        }
    }

    printf(RESET"\n");
    return;
}

bool isnumber(string arg)
{
    // if all characters are digits, it's a number
    int i = 0;
    char c = arg[i];
    int count = 0;

    // loop through all characters, if any are not 
    // a digit then return false
    do
    {
        if (!isdigit(c))
        {
            return false;
        }

        i++;
        c = arg[i];
    }
    while (c != '\0');
    
    return true;    
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
