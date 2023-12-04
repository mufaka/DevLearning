#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    /*
        "to ensure each pixel of the new image still has the same 
        general brightness or darkness as the old image, we can 
        take the average of the red, green, and blue values to 
        determine what shade of grey to make the new pixel."
    */
   
    // loop through the RGBTRIPLEs, average the rgb values and
    // set all the same.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE grayscale = round((image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0);
            image[i][j].rgbtBlue = grayscale;
            image[i][j].rgbtRed = grayscale;
            image[i][j].rgbtGreen = grayscale;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // flip the pixels on row by row basis
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int swap_pixel = width - j - 1;

            // pixel 0 = pixel width - 1, pixel 1 = pixel width - 2, etc.
            // if swap_pixel is greater than j, we can swap.
            if (j >= swap_pixel) 
            {
                // continue to next row
                continue;
            }
            else 
            {
                RGBTRIPLE tmp = image[i][j];
                image[i][j] = image[i][swap_pixel];
                image[i][swap_pixel] = tmp;
            }
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // would be obtained by averaging the ORIGINAL color values of pixels
    // this means that we cannot change in place, we need to calculate all
    // and then replace. ideally we can do this without copying the entire
    // image in memory but not sure how.

    RGBTRIPLE(*blurred_image)[width] = calloc(height, width * sizeof(RGBTRIPLE));

    // 4 nested for loops ... meh.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get the surrounding pixels and sum
            // initially using BYTE as type for sumRed/sumGreen/sumBlue was "fun" ...
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            float count = 0.0;

            // loop through potentially adjacent pixels
            // -1, -1 to +1, +1
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++) 
                {
                    // is i + k, j + l a valid pixel?
                    int test_x = i + k;
                    int test_y = j + l;

                    // make sure we aren't out of bounds
                    if (test_x >= 0 && test_x < height && test_y >= 0 && test_y < width)
                    {
                        sumRed += image[test_x][test_y].rgbtRed;
                        sumGreen += image[test_x][test_y].rgbtGreen;
                        sumBlue += image[test_x][test_y].rgbtBlue;
                        count += 1.0;
                    }
                }
            }

            blurred_image[i][j].rgbtRed = round(sumRed / count);
            blurred_image[i][j].rgbtGreen = round(sumGreen / count);
            blurred_image[i][j].rgbtBlue = round(sumBlue / count);
        }
    }

    // can we swap the pointer to blurred_image? if so, how do we free original image?
    // just loop again for now
    for (int i = 0; i < height; i++) 
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = blurred_image[i][j];

            // printf("Setting Blue to %i from %i\n", blurred_image[i][j].rgbtBlue, image[i][j].rgbtBlue);
            // image[i][j].rgbtRed = blurred_image[i][j].rgbtRed;
            // image[i][j].rgbtGreen = blurred_image[i][j].rgbtGreen;
            // image[i][j].rgbtBlue = blurred_image[i][j].rgbtBlue;
        }
    }

    free(blurred_image);

    return;
}

// NOTE: style50 wants these declarations to be formatted on same line but I think this is more readable.
int GX_KERNEL[3][3] = {
    {-1, 0, 1},
    {-2, 0, 2},
    {-1, 0, 1}
};

int GY_KERNEL[3][3] = {
    {-1, -2, -1},
    {0, 0, 0},
    {1, 2, 1}
};

int limit_value(int min, int max, int val)
{
    if (val < min)
    {
        return min;
    }
    else if (val > max)
    {
        return max;
    }
    else
    {
        return val;
    }
}

int merge_kernels(int x, int y, int original)
{
    int val = round(sqrt(x * x + y * y));
    int new_val = limit_value(0, 255, val);

    return new_val;

    // below is expirimental
    // lets only change the value if there is 
    // a noticeable difference
    // int delta = abs(val - new_val);
    // return delta > 20 ? new_val : original;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE(*edged_image)[width] = calloc(height, width * sizeof(RGBTRIPLE));

    /*
        for each of the three color values for each pixel, we’ll compute two 
        values Gx and Gy. 
        
        To compute Gx for the red channel value of a pixel, 
        for instance, we’ll take the original red values for the nine pixels 
        that form a 3x3 box around the pixel, multiply them each by the 
        corresponding value in the Gx kernel, and take the sum of the resulting 
        values.    

        Do the same for Gy and then combine the values.

        Square root of Gx^2 + Gy^2 capped at 255
    */

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRedGx = 0;
            int sumGreenGx = 0;
            int sumBlueGx = 0;

            int sumRedGy = 0;
            int sumGreenGy = 0;
            int sumBlueGy = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++) 
                {
                    int test_x = i + k;
                    int test_y = j + l;

                    if (test_x >= 0 && test_x < height && test_y >= 0 && test_y < width)
                    {
                        // k and l start at -1 but we need to shift for kernel
                        int gx_weight = GX_KERNEL[k + 1][l + 1];
                        sumRedGx += image[test_x][test_y].rgbtRed * gx_weight;
                        sumGreenGx += image[test_x][test_y].rgbtGreen * gx_weight;
                        sumBlueGx += image[test_x][test_y].rgbtBlue * gx_weight;

                        int gy_weight = GY_KERNEL[k + 1][l + 1];
                        sumRedGy += image[test_x][test_y].rgbtRed * gy_weight;
                        sumGreenGy += image[test_x][test_y].rgbtGreen * gy_weight;
                        sumBlueGy += image[test_x][test_y].rgbtBlue * gy_weight;
                    }
                    else
                    {
                        // we are to treat oob pixels as zero values (black), but this really
                        // just effectively adds a zero to the sum
                    }
                }
            }

            /*
                When we take the sum, if the pixels on the right are a similar color to the 
                pixels on the left, the result will be close to 0 (the numbers cancel out). 
                But if the pixels on the right are very different from the pixels on the left, 
                then the resulting value will be very positive or very negative, indicating 
                a change in color that likely is the result of a boundary between objects. 
                And a similar argument holds true for calculating edges in the y direction.

                It doesn't make sense that we'd calculate the values for the pixel based
                on this. If the sum is zero then the value will be set to zero even if 
                it started at 128 .... we need to leave these cases alone.        
            */

            edged_image[i][j].rgbtRed = merge_kernels(sumRedGx, sumRedGy, image[i][j].rgbtRed);
            edged_image[i][j].rgbtGreen = merge_kernels(sumGreenGx, sumGreenGy, image[i][j].rgbtGreen);
            edged_image[i][j].rgbtBlue = merge_kernels(sumBlueGx, sumBlueGy, image[i][j].rgbtBlue);

            /*
            if (edged_image[i][j].rgbtRed == 255
                && edged_image[i][j].rgbtGreen == 255
                && edged_image[i][j].rgbtBlue == 255
                ) 
            {
                edged_image[i][j].rgbtRed = 255;
                edged_image[i][j].rgbtGreen = 0;
                edged_image[i][j].rgbtBlue = 0;
            }
            else 
            {
                edged_image[i][j].rgbtRed = image[i][j].rgbtRed;
                edged_image[i][j].rgbtGreen = image[i][j].rgbtGreen;
                edged_image[i][j].rgbtBlue = image[i][j].rgbtBlue;
            }
            */
        }
    }

    for (int i = 0; i < height; i++) 
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = edged_image[i][j];
        }
    }

    free(edged_image);

    return;
}
