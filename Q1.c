#include <stdio.h>

int main(void){
	char name[20];
	
	printf("what is your name?\n");
	
	fgets(name,20,stdin);
	
	printf("Hello %s", name);
	
}