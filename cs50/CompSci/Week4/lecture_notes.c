#include <stdio.h>
#include <stdlib.h> // for malloc
#include <string.h>
#include <cs50.h>

// function prototypes
void pointers();
void strings();
void arithmetic();
void string_copy();
void swap_main();
void swap_ints(int *a, int *b);
void use_scanf();
void files();


int main(void) 
{
    pointers();
    strings();
    arithmetic();
    string_copy();
    swap_main();
    use_scanf();
    files();
}

/*
    Base-16
    0 1 2 3 4 5 6 7
    8 9 A B C D E F 

    FF = 255
    16 * F + 1 * F = 240 + 15
*/
void pointers()
{
    // 0x prefix to signify hexadecimal
    int n = 50;
    printf("%i\n", n);

    // but what is really happening? Where is the n stored?
    // it is somewhere taking up 32 bits / 4 bytes and that is at some memory address

    // & -> get the address of. %p format string is used for addresses
    printf("The variable n is stored in memory at %p\n", &n); // 0x7ffe2c96ecbc

    // * -> is a pointer to the address; go there.
    // pointer is a variable that contains the address of some value
    int *p = &n; // p is a pointer. it contains a number that is an address
    printf("The pointer to n is %p\n", p); // 0x7ffe2c96ecbc

    // an interesting side node:
    printf("The pointer variable is stored at %p\n", &p); // print out the address of the pointer. 
}

void strings()
{
    // typedef char *string

    string s = "HI!";
    printf("%p\n", s);      // 0x55d363afa08e <-- this is the same as the address of the first element in the array
    printf("%p\n", &s[0]);  // 0x55d363afa08e                           H
    printf("%p\n", &s[1]);  // 0x55d363afa08f <-- incrementing 1 byte   I
    printf("%p\n", &s[2]);  // 0x55d363afa090 <-- incrementing 1 byte   !
    printf("%p\n", &s[3]);  // 0x55d363afa091 <-- incrementing 1 byte   \0 NUL (end of string)

    // can there be an &s[4]?
    printf("%p\n", &s[4]); // 0x563ac780c092 <-- overflow; this works for getting the address. What is there?
    printf("%i\n", s[0]);  // 72 ascii code for H
    printf("%i\n", s[1]);  // 73 ascii code for I
    printf("%i\n", s[2]);  // 33 ascii code for !
    printf("%i\n", s[3]);  // 0  ascii code for NUL
    printf("%i\n", s[4]);  // 37 ascii code for % but we don't know the type or what this value is used for
}

void arithmetic()
{
    // string is just a char *
    char *s = "HI!";
    printf("%c\n", *s); // NOTE: the pointer s points to the first address of the char array
    printf("%c\n", *(s + 1)); // increment the pointer address by 1
    printf("%c\n", *(s + 2));
    printf("%c\n", *(s + 3));
    printf("%c\n", *(s + 4));
}

void string_copy()
{
    char *s = "Hello, this is a string to copy.";

    // malloc allocates some memory to use.
    char *t = malloc(strlen(s) + 1); // strlen returns the length of the string without NUL terminator

    printf("\n");
    printf("----string_copy----\n");
    printf("The address of t is %p\n", t);

    for (int i = 0, n = strlen(s); i <= n; i++) 
    {
        // what random value is in t[i] before assignment?
        // the following results in all zeros but malloc itself doesn't do so (calloc does).
        // It's up to the compiler to determine what to do here. The takeaway is that you 
        // shouldn't assume a zero initilized value from malloc. Or maybe it does when
        // assigning to a char *. 

        // the following is detected by valgrind
        //printf("Value before assignment of t[%i] is char %c, int %i\n", i, t[i], t[i]);

        t[i] = s[i];
    }

    printf("%s\n", t);

    // IMPORTANT! If you malloc, you should free otherwise you have a memory leak.
    // Consider the case where you repeatedly call this function and don't free(t)...
    // malloc will keep finding new address space to use. 
    free(t);

    // valgrind is a tool that can check for memory related issues.
    // sudo apt install valgrind
    // it tests the compiled program, not source code.
    // valgrind ./lecture_notes

    // if the memory is freed for t, what happens if we try to print it again?
    // the following results in garbage. so we still have the pointer to the address
    // but the values have been randomized? At any rate, the important thing to know
    // is that free makes the address usable again for other mallocs.

    // the following is detected by valgrind
    //printf("%s\n", t);
}

void swap_main()
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap_ints(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap_ints(int *a, int *b)
{
    // pointers are in the heap so we can do this
    // we are just swapping pointers (that hold the address)
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void use_scanf()
{
    // cs50.h provided get_int, get_string, etc as training wheels.
    // scanf is how you get user input..

    int x; 
    printf("x: ");
    scanf("%i", &x); // %i means get an int, &x means here is the address to store it at...
    printf("%i\n", x);

    // strings are more difficult. You need to allocate memory for them before asking...
    char s[4];
    printf("s: ");
    scanf("%s%*c", s); // NOTE: don't need & here because strings are "special"
    printf("%s\n", s);

    // NOTE: if user enters more than 4 characters, fun happens. *** stack smashing detected ***: terminated
    // probably should just use a library for that...no reason to re-invent the wheel for such a "should be for free" feature.
}

void files()
{
    // Get name and number... this doesn't seem to be waiting for name input, just shows both as Name: Number:
    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    // scanf from previous function is messing up the above two lines. It seems like an extra char (NUL?) is being fed to the input for *name....
    // maybe because I have been typing 3 characters for the scanf prompt but allocating space for 4? No...maybe it's the \n?
    // scanf sucks ... you need to "consume" the next char ... scanf("%s%*c")

    // create a file and write to it...
    FILE *file = fopen("phonebook.csv", "a"); // what is a? https://www.man7.org/linux/man-pages/man3/fopen.3.html; means append

    // Print to file - fprintf. auto-flushes I guess.
    fprintf(file, "%s,%s\n", name, number);

    // Close file
    fclose(file);
}