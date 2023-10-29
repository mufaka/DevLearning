#include <stdio.h>
#include <stdbool.h> // cs50.h does this as well, includes true / false 

int main(void)
{
    int i = 0;

    while (i < 10)
    {
        printf("while meow\n");
        i++;
    }

    for (int x = 0; x < 3; x++)
    {
        printf("for meow\n");
    }
}