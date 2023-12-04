#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates[8];

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // we can't just add buffer to plates, its
        // an address that keeps getting used

        // malloc allocates on heap so will need to be freed
        char *plate = malloc(sizeof(buffer));
        strcpy(plate, buffer);

        // Save plate number in array
        plates[idx] = plate;
        idx++;
    }

    // we are done with the file
    fclose(infile);

    for (int i = 0; i < 8; i++)
    {
        printf("%s\n", plates[i]);
        free(plates[i]);
    }

    // this doesn't work because we didn't alloc plates
    // free(plates);
}
