#include <cs50.h>
#include <stdio.h>

int getPopulationSize(string prompt, int min);
int getYearsUntilPopulationSize(int startSize, int endSize);
int getPopulationGrowth(int size);

int main(void)
{
    /*
        Your program should first prompt the user for a starting population size.
            If the user enters a number less than 9 (the minimum allowed population size), 
            the user should be re-prompted to enter a starting population size until they enter a number that is greater than or equal to 9. 
            (If we start with fewer than 9 llamas, the population of llamas will quickly become stagnant!)    
    */
    // TODO: Prompt for start size
    int startSize = getPopulationSize("Start size: ", 9);
    // TODO: Prompt for end size
    int endSize = getPopulationSize("End size: ", startSize);

    // TODO: Calculate number of years until we reach threshold
    // n / 3 added each year, n / 4 removed each year but also realize that each year you start with more than previous year
    // loop until startSize >= endSize
    int years = getYearsUntilPopulationSize(startSize, endSize);


    // TODO: Print number of years
    printf("Years: %i\n", years);
}

int getPopulationSize(string prompt, int min)
{
    int size;

    do 
    {
        size = get_int("%s", prompt);
    }
    while (size < min);

    return size;
}

int getYearsUntilPopulationSize(int startSize, int endSize)
{
    int years = 0;

    if (startSize == endSize) return years;
    
    do
    {
        startSize += getPopulationGrowth(startSize);
        years++;
    }
    while (startSize < endSize);

    return years;
}

int getPopulationGrowth(int size)
{
    int births = size / 3;
    int deaths = size / 4;

    return births - deaths;
}
