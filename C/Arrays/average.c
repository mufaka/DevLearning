#include<stdio.h>

/*
gcc average.c -o average.out
./average.out
*/

int main(void) 
{
    int score1 = 72; // 4 bytes
    int score2 = 73; // 4 bytes
    int score3 = 33; // 4 bytes

    printf("Average: %f\n", (score1 + score2 + score3) / 3.0f);

    // use an array instead of declaring arbitrary amounts of variables.
    int scores[] = { 72, 73, 33 }; // 12 contiguous bytes.

    int i; 
    int total;
    int scores_length = sizeof(scores) / sizeof(scores[0]);
    int pointer_length = *(&scores + 1) - scores;

    printf("Array length: %i\n", scores_length);
    printf("Pointer length: %i\n", pointer_length);

    for (i = 0; i < scores_length; ++i) 
    {
        total += scores[i];
        printf("Total: %i, %i\n", total, scores[i]);
    }

    printf("Total: %i\n", total);
    printf("Average: %f\n", (float)total / scores_length);
    return 0;
}