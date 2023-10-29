#include <cs50.h>
#include <stdio.h>


int main(void)
{
    long int x = get_int("X? ");
    long int y = get_int("Y? ");

    // 2 billion plus 2 billion results in signed integer overflow error if type is int, change to long integer

    /*
        %c char
        %f float
        %i integer
        %s string
        
        %li long integer
    */

    // long goes up to 9 quintillion! 9223372036854775807

    printf("%li\n", (x + y));

    // truncation. lose values after decimal 
    // if 1 / 3 answer is zero (need float type)
    printf("%li\n", (x / y));

    // floating-point imprecision: 1/3 = 0.33333334326744079590
    //  approximates because only a finite way to represent it

    float z = (float) x / (float) y;
    // NOTE: format syntax is %.20f (20 digits after decimal)
    printf("%.20f\n", z);

    double d = (double) x / (double) y;
    // double is more precise (uses, currently, 64 bits vs float 32 bits)
    // 0.33333333333333331483
    printf("%.20f\n", d);

    // seconds since epoch (1/1/1970) will overflow on 1/19/2038 (less than 15 years from now). It's the next Y2K bug.

}