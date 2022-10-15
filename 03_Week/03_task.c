// To compute the sum of the two given integers. If the sum is in the range 10..20 
// inclusive return 30

#include <stdio.h>

int sumNumbers(int a, int b)
{
    int sum = 0;
	sum = a + b;
	
	if (sum > 9 && sum < 21 )
        {
         sum = 30;
        }
	return sum;
}



int main(void){
    //int a = 5;
    //int b = 5;
    
    int a = 0;
    int b = 0;

    printf("Enter first number\n");
	scanf("%d", &a);

    printf("Enter second number\n");
	scanf("%d", &b);
    
    int s = sumNumbers(a, b);
	
	printf("%d",s);
    
    return 0;
}