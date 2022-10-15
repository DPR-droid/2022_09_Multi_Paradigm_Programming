#include <stdio.h>

int sumNumbers(int n)
{
	int sum = 0;
	
	for(int i = 0; i<=n; i++)
	{
		sum += i;
	}	
	
	return sum;
}

int main(void){
	
	int n = 0;
	
	printf("Enter a number\n");
	scanf("%d", &n);
	
	int s = sumNumbers(n);
	
	printf("the sum of 1 to %d is %d\n", n, s);
	
}