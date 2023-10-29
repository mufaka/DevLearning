#include <stdio.h>
#include <cs50.h>

// if the function is declared after it's use, you need to
// provide a function declaration
int get_size(string prompt, int min);
void print_grid(int rows, int cols);

int main(void)
{
    // const makes variable immutable
    // const int rows = 13;
    // const int cols = 14;
    /*
    int rows;
    int cols;

    do
    {
        rows = get_int("Rows? ");
    }
    while (rows < 1);

    do
    {
        cols = get_int("Cols? ");
    }
    while (cols < 1);
    */

    // use a function instead 
    int rows = get_size("Rows? ", 1);
    int cols = get_size("Cols? ", 1);
    print_grid(rows, cols);
}

int get_size(string prompt, int min)
{
    int val;

    do
    {
        // NOTE: need to pass format string and val to get_int because
        //       it expects a string literal and we are passing in a variable.
        //       This is a little wonky to think about but consider the case
        //          where a malicious string format is provided here (%s or %n will read and write from invalid memory)
        val = get_int("%s", prompt);
    }
    while (val < min);

    return val;
}

void print_grid(int rows, int cols)
{
    for (int x = 0; x < rows; x++) 
    {
        for (int y = 0; y < cols; y++)
        {
            printf("#");
        }
        printf("\n");
    }
}

