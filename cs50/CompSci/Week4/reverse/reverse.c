#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // refer to volume.c from a previous exercise for
    // reading a .wave file and bottomup.c / bmp.h
    // for reading into a struct

    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open input file %s.\n", argv[1]);
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER wh;
    fread(&wh, sizeof(WAVHEADER), 1, input);

    // Use check_format to ensure WAV format
    // TODO #4
    if (!check_format(wh))
    {
        printf("Input file is not in WAVE format.\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open output file %s.\n", argv[2]);
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&wh, sizeof(WAVHEADER), 1, output);    

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(wh);

    // Write reversed audio to file
    // TODO #8
    // at this point, we've read past the header in input,
    // the rest is data. fread moves a 'cursor' so we are
    // ready to read the rest of the data. 

    // create a buffer for a single block
    BYTE block[block_size];

    // seek to the end of the file minus block size to 
    // get to last block
    fseek(input, 0 - block_size, SEEK_END);
    int position = ftell(input);

    do 
    {
        // printf("Current position is %i\n", position);
        fread(&block, block_size, 1, input);
        fwrite(&block, block_size, 1, output);

        // now that we've read again, position is at
        // end of block. need to got to beginning of
        // prior block. (2 * size of block)
        fseek(input, 0 - block_size * 2, SEEK_CUR);
        position = ftell(input);
    } 
    while (position >= sizeof(wh));

    fclose(input);
    fclose(output);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    // wh.format should equal WAVE
    // it seems there should be a better way
    if (header.format[0] == 87      // W
        && header.format[1] == 65   // A
        && header.format[2] == 86   // V
        && header.format[3] == 69)  // E
    {
        return 1;
    }

    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    // For audio, we calculate the size of each block with the following calculation: 
    // number of channels multiplied by bytes per sample.
    // printf("Bits per sample: %i, Num Channels: %i\n", header.bitsPerSample, header.numChannels);
    // 16 bits, 2 channels. 4 bytes per block
    return (header.bitsPerSample / 8) * header.numChannels;
}