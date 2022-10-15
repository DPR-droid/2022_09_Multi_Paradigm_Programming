// to check if y is greater than x, and z is greater than y from three given integers x, y, z. Print
// appropriate messages using printf()

#include <stdio.h>

int whichIsGreater(int x, int y, int z)
    {
    if (y > x)
        printf("%d is greater than %d\n", y, x);
    if (z > y)
        printf("%d is greater than %d", z, y);
    }


int main(void)
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

    whichIsGreater(x, y, z);
    
    return 0;

}