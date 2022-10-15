// that accepts two integers and returns true if either one is 5, or their sum, or difference, is 5.

#include <stdio.h>

int fiveNumbers(int a, int b)
{
	int x = 0;
	
	if (a == 5 || b == 5 || (a + b == 5) || (a - b == 5))
        {
        x = 1;
        }
	
	return x;
}


int main(void){
    
    int a = 0;
    int b = 0;

    printf("Enter first number\n");
	scanf("%d", &a);

    printf("Enter second number\n");
	scanf("%d", &b);

    int x = fiveNumbers(a, b);

    if (x == 1) printf("True\n");
    else printf("False\n");
    
    return 0;

}