// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // WAV files begin with a 44-byte “header” that contains information about the file itself, 
    // including the size of the file, the number of samples per second, and the size of each 
    // sample. After the header, the WAV file contains a sequence of samples, each a single 
    // 2-byte (16-bit) integer representing the audio signal at a particular point in time.

    // http://soundfile.sapp.org/doc/WaveFormat/

    // TODO: Copy header from input file to output file
    uint8_t header_buff[HEADER_SIZE];
    fread(header_buff, 1, 44, input);
    fwrite(header_buff, 1, 44, output);

    // TODO: Read samples from input file and write updated data to output file
    // now read 2 byte chunks, multiply by scale factor, and write to output.
    int16_t sample;

    while (fread(&sample, sizeof(int16_t), 1, input))    
    {
        sample = sample * factor;
        fwrite(&sample, sizeof(int16_t), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
