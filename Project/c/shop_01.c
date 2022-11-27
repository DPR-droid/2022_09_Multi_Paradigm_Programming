// Multi-Paradigm Programming Shop Project 
// Build a simulation of a shop in C


// C libraries 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//  Entities
// 		Product
// 		ProductStock
// 		Shop
// 		Customer

// What is a structure? 
// A structure is a key word that create user defined data type in C/C++. 
// A structure creates a data type that can be used to group items of possibly different types into a single type. 
// https://www.geeksforgeeks.org/structures-c/
// Extra line

struct Product {
	char* name; 							// Make name a pointer as unknown lenght of customer name 
	double price;  							// Make a double to include a decimal point
};

struct ProductStock {
	struct Product product;
	int quantity;
};

struct Shop {
	double cash;  							// Make a double to include a decimal point
	struct ProductStock stock[20];
	int index;
};

struct Customer {
	char* name; 							// Make name a pointer as unknown lenght of customer name 
	double budget; 							// Make a double to include a decimal point
	struct ProductStock shoppingList[10];
	int index;
};

//

void printProduct(struct Product p)
{
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	// printf("-------------\n");
}

// void printCustomer(struct Customer c)
// {
// 	printf("CUSTOMER NAME: %s \nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
// 	printf("-------------\n");
// 	for(int i = 0; i < c.index; i++)
// 	{
// 		printProduct(c.shoppingList[i].product);
// 		printf("%s ORDERS %d OF ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity);
// 		double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price; 
// 		printf("The cost to %s will be €%.2f\n", c.name, cost);
// 	}
// }


// Create Stock from CSV file

struct Shop createAndStockShop()
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("../stock.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

	// Issue compiling in windows getline not recognised
	// To compile install WSL2 
	// https://ubuntu.com/tutorials/working-with-visual-studio-code-on-ubuntu-on-wsl2#1-overview


	read = getline(&line, &len, fp);
	float cash = atof(line);
	// printf("cash in shop is %.2f\n", cash);
	
	struct Shop shop = { cash };

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);
        // printf("%s IS A LINE", line);
		char *n = strtok(line, ",");
		char *p = strtok(NULL, ",");
		char *q = strtok(NULL, ",");
		int quantity = atoi(q);
		double price = atof(p);
		char *name = malloc(sizeof(char) * 50);
		strcpy(name, n);
		struct Product product = { name, price };
		struct ProductStock stockItem = { product, quantity };
		shop.stock[shop.index++] = stockItem;
		// printf("NAME OF PRODUCT %s PRICE %.2f QUANTITY %d\n", name, price, quantity);
    }
	
	return shop;
}


void printShop(struct Shop s)
{
	printf("Shop has %.2f in cash\n\n", s.cash);
	printf("-------------\n");
	for (int i = 0; i < s.index; i++)
	{
		printProduct(s.stock[i].product);
		printf("The shop has %d of the above\n", s.stock[i].quantity);
		printf("-------------\n\n");
	}
}


// Read and print customer file
// Use Week 4 to create reading in customer.csv file.

struct Customer customer_file()
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("../customer.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

	// Issue compiling in windows getline not recognised
	// To compile install WSL2 
	// https://ubuntu.com/tutorials/working-with-visual-studio-code-on-ubuntu-on-wsl2#1-overview

	// Read firstline of csv file and get Name and Budget
	read = getline(&line, &len, fp);
	char *name = strtok(line, ",");
	float budget = atof(strtok(NULL, ","));
	// printf("name %s cash for shopping is %.2f\n", name, budget);
	
	struct Customer custlist = { name, budget };

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("\n%s IS A LINE\n", line);
		char *n = strtok(line, ",");
		char *q = strtok(NULL, ",");
		int quantity = atoi(q);

		char *pname = malloc(sizeof(char) * 50);
		strcpy(pname, n);
		struct Product product = { pname, 0 };
		struct ProductStock stockItem = { product, quantity };
		custlist.shoppingList[custlist.index++] = stockItem;

    }
	return custlist;
}

void printCustomer(struct Customer c)
{
	printf("name %s cash for shopping is %.2f\n", c.name, c.budget);
	printf("-------------\n");
	for (int i = 0; i < c.index; i++)
	{
		printProduct(c.shoppingList[i].product);
		printf("The Customer wants %d of the above\n", c.shoppingList[i].quantity);
		printf("-------------\n\n");
	}
}


// Add Menu
// https://www.studytonight.com/c/programs/misc/menu-driven-program

int main()
{
    printf("\n\n\t\tStudytonight - Best place to learn\n\n\n");
    int choice, num, i;
    unsigned long int fact;

    while(1)
    {
        printf("1. Stock in Shop \n");
        printf("2. Customer Shopping List\n");
        printf("3. Odd\\Even\n");
        printf("4. Exit\n\n\n");
        printf("Enter your choice :  ");
        scanf("%d",&choice);
        
        switch(choice)
        {
            case 1:
                {
				struct Shop shop = createAndStockShop();
				printShop(shop);
				}
                break;
        
            case 2:
				{
				struct Customer shoppinglist = customer_file();
				printCustomer(shoppinglist);
				//customer_file();
				}
                break;
        
            case 3:
                break;
        
            case 4:
                printf("\n\n\t\t\tCoding is Fun !\n\n\n");
                exit(0);    // terminates the complete program execution
        }
    }
    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}