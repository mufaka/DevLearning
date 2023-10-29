// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, int tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

float half(float bill, float tax, int tip)
{
    // 12.50 8.875 20 = 8.17
    // 23.50 7 15 = 14.46
    // 100 6.25 18 = 62.69
    float taxAmount = bill * (tax / 100.0);
    float withTax = bill + taxAmount;
    float withTip = withTax + (withTax * ((float)tip / 100.0));

    return withTip / 2.0;
}
