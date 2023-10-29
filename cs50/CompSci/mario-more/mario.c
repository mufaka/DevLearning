#include <cs50.h>
#include <stdio.h>

int main(void) 
{
    int height;

    do
    {
        height = get_int("Height: ");
    }   
    while (height < 1 || height > 8);

    /*
        determine the spacing. 

        01234567
          #  #
         ##  ##
        ###  ###
    
        first block starts at a space that matches height - row - 1
    */
    for (int i = 0; i < height; i++)
    {
        int firstBlockIndex = height - i - 1;

        // build left side; feels like there should be some type of padding function
        // but manually do it instead.
        for (int j = 0; j < height; j++)
        {
            if (j >= firstBlockIndex)
            {
                printf("#");
            }
            else 
            {
                printf(" ");
            }
        }

        // two space gap
        printf("  ");

        // build right side
        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}