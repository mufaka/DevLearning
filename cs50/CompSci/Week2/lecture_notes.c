#include <cs50.h>
#include <stdio.h>

/*
    Week2 is Arrays

    U I J T  X B T  D T 5 0  (cypher text)
    T H I S  W A S  C S 5 0 (letters subtract 1, numbers subtract 0)

    Talk about what make is doing:
        clang -o hello hello.c -lcs50  (-lxxxx -l means link, cs50 means link cs50.h output)

        I use gcc with make, configured in ~/.bashrc as follows:

        # cs50 library
        export CC="gcc"
        export CFLAGS="-fsanitize=signed-integer-overflow -fsanitize=undefined -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow"
        export LDLIBS="-lcrypt -lcs50 -lm"(base)        

        so when make is run, it uses gcc, adds the compiler flags (CFLAGS), and adds the linked libraries (LDLIBS)

        $make hello
        gcc -fsanitize=signed-integer-overflow -fsanitize=undefined -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow    hello.c  -lcrypt -lcs50 -lm -o hello

        Probably not the best solution to use ./bashrc because that is global. Good enough to work with cs50 though.

        /usr/include is typically where libraries are located.


        building (compiling):
            preprocessing - combine all source files
            compiling - generates assembly language
            assembling - binary file that includes only your code
            linking - including binary from external libraries

        decompiling:
            You won't get original source code because symbol names aren't retained
*/

void buggy0();
void buggy1();
void datatypes();
void memory();
void arrays();
float average(int array[], int arraySize);
void strings();
int stringLength(string str);
void uppercase(string str, string t);
void twice();

// arg c is count, argv is values
int main(int argc, string argv[]) 
{
    memory();
    arrays();
    strings();

    if (argc > 0) 
    {
        for (int i = 0; i < argc; i++) 
        {
            printf("%s\n", argv[i]);
        }
    }

    twice();

    /*
        You can declare multiple variables in the for loop
        for (int i = 0; n = strlen(s); i < n; i++)
    */
   /*
    echo $?
   */
   return 0;
}

/*
Print Debugging

buggy0 is supposed to print 3 # (one per line)
*/
void buggy0()
{
    for (int i = 0; i <= 3; i++)
    {
        // print debugging
        printf("i is %i", i);
        printf("#\n");
    }    
}

/*
    VS Code Debugger

    Need to add appropriate configuration to launch.json for the language
    you are debugging.
*/
void buggy1()
{
    for (int i = 0; i <= 3; i++)
    {
        printf("#\n");
    }    
}

void dataTypes() 
{
    bool yesNo; // 1 byte; only need 1 bit but need to have a base 
    int int1; // 4 bytes (32 bit) 4 billion, -2 billion to 2 billion
    long long1; // 8 bytes a quintillion number of possibilities (even so, it's finite)
    float float1; // 4 bytes -> decimal point. specific amount of precision
    double double1; // 8 bytes -> decimal point. more digits of precision but still not precise
    char char1; // 1 byte
    string string1; // ? bytes; actuall a char *[]; cs50 defines it for you. cat /usr/include/cs50.h -> typedef char *string;
}

void memory() 
{
    int score1 = 72; // 4 bytes
    int score2 = 73; // 4 bytes
    int score3 = 33; // 4 bytes

    printf("Average: %f\n", (score1 + score2 + score3) / 3.0); // just one value needs to be float
}

void arrays() 
{
    // stores data back to back to back in memory
    int scores1[3];
    scores1[0] = 72;
    scores1[1] = 73;
    scores1[2] = 33;

    printf("Scores 1 Average: %f\n", (scores1[0] + scores1[1] + scores1[2]) / 3.0);

    /*
    const int scoresSize = 3;
    int scores2[scoresSize];

    for (int i = 0; i < scoresSize; i++) 
    {
        scores2[i] = get_int("Score: ");
    }

    // printf("Scores 2 Average: %f\n", (scores2[0] + scores2[1] + scores2[2]) / 3.0);
    printf("Scores 2 Average: %f\n", average(scores2, scoresSize));
    */
}

float average(int array[], int arraySize) 
{
    float total = 0;

    for (int i = 0; i < arraySize; i++) 
    {
        total += array[i];
    }

    return total / (float)arraySize;
}

void strings() 
{
    // string is an array of characters that end with a NUL \0 character.
    string s = "Hi!";
    printf("%c%c%c\n", s[0], s[1], s[2]);

    string t = "I am a 27 character string!";
    printf("%s is %i characters long.\n", t, stringLength(t));
    char upper[stringLength(t)];
    uppercase(t, upper);
    printf("%s\n", upper);
}

int stringLength(string str)
{
    int n = 0;

    while (str[n] != '\0')
    {
        n++;
    }

    return n;
}

// it would be nice to figure out how to modify the 
// str variable in place. Passing in a separate char * 
// is the only way I can get this to work for now ...
void uppercase(string str, string upper)
{
    int i = 0;
 
    while (str[i] != '\0')
    {
        if (str[i] >= 'a' && str[i] <= 'z')
        {
            upper[i] = str[i] - 32;
        }
        else 
        {
            upper[i] = str[i];
        }

        i++;
    }

    upper[i] = '\0';
}

void twice() 
{
    int length = 10;

    int twos[length];
    twos[0] = 1;
    printf("%i\n", twos[0]);

    for (int i = 1; i < length; i++) 
    {
        twos[i] = 2 * twos[i - 1];
        printf("%i\n", twos[i]);
    }
}