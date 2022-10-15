#include <stdio.h>
#include <string.h>

int main(void){
	char name[20];
	
	printf("what is your name?\n");
	
	fgets(name,20,stdin);

	name[strcspn(name,"\n")] = '\0';
	
	if ((strcmp(name, "Alice") == 0) || (strcmp(name, "Bob") == 0))
	{
		printf("Hello %s!\n", name);
	}
	else 
	{
		printf("Hello Peasant!\n");
	}
	
}