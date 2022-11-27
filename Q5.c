#include <stdio.h>
#include <string.h>

int sumOfNumbers(int n)
{
	int sum = 0;
	
	for(int i = 0; i<=n; i++)
	{
		
		sum += i;
	}	
	
	return sum;
}

int productOfNumbers(int n)
{
	int product = 1;
	
	for(int i = 1; i<=n; i++)
	{
		
		product *= i;
	}	
	
	return product;
}

int main(void){
	
	int n = 0;
	char name[20];
	
	printf("Enter a number\n");
	scanf("%d", &n);
	
	// clear the input buffer
	while ((getchar()) != '\n');
	
	printf("do you want to calculate product or sum?\n");
	fgets(name,20,stdin);

	// clears the \n from name variable
	name[strcspn(name,"\n")] = '\0';
	
	if ((strcmp(name, "sum") == 0))
	{
		int s = sumOfNumbers(n);
		printf("the sum of 1 to %d is %d\n", n, s);
	} 
	else if ((strcmp(name, "product") == 0)) 
	{
		int p = productOfNumbers(n);
		printf("the product of 1 to %d is %d\n", n, p);
	} 
	else 
	{
		printf("the program does not understand what you want");
	}
		
	
}