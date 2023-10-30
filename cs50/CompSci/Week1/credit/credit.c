#include <cs50.h>
#include <stdio.h>

bool isValidCardNumber(long cardNumber);
string getCardType(long cardNumber);

int main(void) 
{
    long int cardNumber = get_long("Number: ");
    //long cardNumber = 378282246310005;

    if (!isValidCardNumber(cardNumber))
    {
        printf("INVALID\n");
    }
    else 
    {
        string cardType = getCardType(cardNumber);
        printf("%s\n", cardType);
    }
}

bool isValidCardNumber(long cardNumber)
{
    int position = 1;
    int digit;
    int luhnSum = 0; // NOTE: This NEEDS ASSIGNED because otherwise it is just using whatever value happens to be at the address allocated
                     //       and we are just using +=. Note that digit variable above does not need this because we have a proper assignment.
                     //       This was 'fun' to figure out.


    /*
        Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
        Add the sum to the sum of the digits that weren’t multiplied by 2.
        If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!    
    */
    while (cardNumber > 0)
    {
        // mod 10 effectively gives us the last digit
        digit = cardNumber % 10;
    
        if (position % 2 == 0)
        {
            int doubled = digit * 2;

            // get the sum of the digits in the product and add to the running total (luhnSum)
            int secondDigit = doubled % 10;
            int firstDigit = doubled / 10;
            luhnSum += (firstDigit + secondDigit);
        }
        else
        {
            luhnSum += digit;
        }

        // dividing by 10 effectively removes the last digit (because it's dealing with whole number)   
        cardNumber = cardNumber / 10;
        position++;
    }

    return luhnSum % 10 == 0;
}

string getCardType(long cardNumber)
{
    // keep dividing by 10 until the number is less than 100
    long temp = cardNumber;
    int numberCount = 2;

    while (temp >= 100)
    {
        temp = temp / 10;
        numberCount++;
    }

    // temp is now a 2 digit number.

    /*
        All American Express numbers start with 34 or 37 
        Most MasterCard numbers start with 51, 52, 53, 54, or 55 
        All Visa numbers start with 4    
    */
    if (temp == 34 || temp == 37)
    {
        if (numberCount == 15)
        {
            return "AMEX";
        }
    }
    else if (temp >= 51 && temp <= 55)
    {
        if (numberCount == 16)
        {
            return "MASTERCARD";
        }
    }
    else if (temp >= 40 && temp <= 49)
    {
        if (numberCount == 13 || numberCount == 16)
        {
            return "VISA";
        }
    }

    return "INVALID";
}