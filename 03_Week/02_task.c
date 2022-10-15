// To check two given integers, and return true if one of them is 30 or if their sum is 30. C doesn’t
// have booleans built-in, so you can use the snippet in Listing 2 or use the values 1 and 0

#include <stdio.h>
#include <stdbool.h> // Header file for boolean data-type.


int main(){

    bool x = false;
    
    int a = 0;
    int b = 0;

    printf("Enter first number\n");
	scanf("%d", &a);

    printf("Enter second number\n");
	scanf("%d", &b);

    if (a == 30 || b == 30 || (a + b == 30))
        {
        x = 1;
        printf("Value = %d\n", x); 
        }
    else 
        {
        printf("Value = %d\n", x);
        }
    
    return 0;

}