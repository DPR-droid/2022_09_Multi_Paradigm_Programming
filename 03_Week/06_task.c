// To check if two or more non-negative given integers have the same rightmost digit.

#include <stdio.h>

int nonNegative(int x, int y, int z)
{

	if (x % 10 == y % 10 || x % 10 == z % 10 || y % 10 == z % 10)
        {
        x = 1;
        }
	
	return x;
}

int main()
{
    int x = 0;
    int y = 0;
    int z = 0;

    printf("Enter first number\n");
	scanf("%d", &x);

    printf("Enter second number\n");
	scanf("%d", &y);

    printf("Enter second number\n");
	scanf("%d", &z);

    int a = nonNegative(x, y, z);

    if (a == 1) printf("True\n");
    else printf("False\n");
    
    return 0;

}