#include <stdio.h>
#include <cs50.h>

/*
gcc lecture_notes.c -o lecture_notes.out
    or 'make lecture_notes' which does the same thing exception output is just 'lecture_notes'
./lecture_notes.out

quality of code: 
    correctness, 
    design, 
    style


cs50 provides a helper that is used in the course (cs50.h)
$ curl -s https://packagecloud.io/install/repositories/cs50/repo/script.deb.sh | sudo bash
$ sudo apt-get install libcs50

Add the following to ~/.bashrc
# cs50 library
 export CC="gcc"
 export CFLAGS="-fsanitize=signed-integer-overflow -fsanitize=undefined -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow"
 export LDLIBS="-lcrypt -lcs50 -lm"

Reload 
$ source ~/.bashrc 

printf %[flags][width][.precision][length]specifier
specifier defines the type and interpretation of it's corresponding argument
Types in c (some)
    bool
    char    c
    double
    float   f
    int     d or i, signed decimal integer; u unsigned decimal integer
    long
    string  s



*/

int main(void) 
{
    string first = get_string("What's your first name? ");
    string last = get_string("What's your last name? ");
    printf("hello, %s %s\n", first, last);

    printf("You have to escape a %% sign with %%%%.\n");
}