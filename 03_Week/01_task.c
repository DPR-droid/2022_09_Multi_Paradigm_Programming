// To calculate the absolute difference between n and 51. If n is greater than 51 return triple the
// absolute difference.

#include <stdio.h>
#include <stdlib.h>


int absNumbers(int n)
{
	const int x = 51;

    if (n > x)
    {
        return (n - x)*3;
    }
    return x - n;
}

int main(void)
{
    int n = 0;

    printf("Enter first number\n");
	scanf("%d", &n);

    int a = absNumbers(n);
    printf("Absolute value = %d\n", a);
    return 0;
}
