#include <stdio.h>

/*
gcc average.c -o average.out
./average.out
*/

// need to define the function and implement below
float array_average(int length, int array[]);

int main(void) 
{
    int score1 = 72; // 4 bytes
    int score2 = 73; // 4 bytes
    int score3 = 33; // 4 bytes

    printf("Average: %f\n", (score1 + score2 + score3) / 3.0f);

    int scores[] = { 72, 73, 33 }; // 12 contiguous bytes.

    // a couple of different ways to get length of array
    int array_length = sizeof(scores) / sizeof(scores[0]);
    int pointer_length = *(&scores + 1) - scores;

    float average = array_average(array_length, scores);

    printf("Average: %f\n", average);
    return 0;
}

// you have to pass the length of the array here
// because it doesn't seem possible to use the
// above means to get the length of the array.
float array_average(int length, int array[]) 
{
    int total;

    for (int i = 0; i < length; ++i) 
    {
        total += array[i];
        printf("Total: %i, %i\n", total, array[i]);
    }

    printf("Total: %i\n", total);

    return (float)total / length;
}