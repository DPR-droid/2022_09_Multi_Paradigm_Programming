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

struct ProductStock {						// nested struct ProductStock
	struct Product product;					// nested to Product
	int quantity;							// Quantity of Product
};

struct Shop {
	double cash;  							// Make a double to include a decimal point
	struct ProductStock stock[20];			// nested to ProductStock
	int index;								// index for Products
};

struct Customer {
	char* cname; 							// Make name a pointer as unknown lenght of customer name 
	double budget; 							// Make a double to include a decimal point
	struct ProductStock shoppingList[10];	// nested to ProductStock Customer Shopping List
	int index;								// index for Products
};

//

void printProduct(struct Product p)
{
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
	// printf("-------------\n");
}



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


void printShop(struct Shop* s)
{
	printf("Shop has %.2f in cash\n\n", s->cash);
	printf("-------------\n");
	for (int i = 0; i < s->index; i++)
	{
		printProduct(s->stock[i].product);
		printf("The shop has %d of the above\n", s->stock[i].quantity);
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

	char *cn = strtok(line, ",");
	char *cname = malloc(sizeof(char) * 50);
	strcpy(cname, cn);

	float budget = atof(strtok(NULL, ","));
	// printf("name %s cash for shopping is %.2f\n", name, budget);
	
	struct Customer custlist = { cname, budget };

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("\n%s IS A LINE\n", line);
		char *n = strtok(line, ",");
		char *q = strtok(NULL, ",");
		int quantity = atoi(q);

		char *pname = malloc(sizeof(char) * 50);
		strcpy(pname, n);
		struct Product product = { pname };
		struct ProductStock stockItem = { product, quantity };
		custlist.shoppingList[custlist.index++] = stockItem;

    }
	return custlist;
}



void storeCheck(){
	
}

// Read in customer orders from a CSV file.
// 		That file should include all the products they want and the quantity.
// 		It should also include their name and budget.
// Edited from 
// MPP - Week 4 - Shop in C Part 2.mov
void printCustomer(struct Customer c, struct Shop* s)
{
	printf("Customer name is %s and the budget for shopping is %.2f\n", c.cname, c.budget);
	printf("-------------\n");
	
	// Set the variable for the total cost of Customer bill.
	double total = 0;

	for (int a = 0; a < c.index; a++)
	{
		
		//https://www.geeksforgeeks.org/strcmp-in-c-cpp/
		// Set Check for item in shop
		int res = 0;

		//printf("The Customer wants %d of %s\n", c.shoppingList[i].quantity, c.shoppingList[i].product.name);
		double cusBud = c.budget;
		char *cusItem = c.shoppingList[a].product.name;
		int cusQuan = c.shoppingList[a].quantity;

		//printf("The output 1 name is %d, for %s\n", res, cusItem);

		// printf("The product name is  %s\n", c.shoppingList[a].product.name);
		// Edited from 
		// MPP - Week 8 - C - Passing Arguments As Pointer.mov
		// ProductStock.c
		for (int b = 0; b < s->index; b++)
			{

				//printf("The output 1 name is %d\n", strcmp(cusItem, s->stock[b].product.name));	
				
				if (strcmp(s->stock[b].product.name, cusItem ) == 0)
				{
					// If item in shop set res to 1
					res = 1;
					//printf("The output 2 name is %d\n", strcmp(cusItem, s->stock[b].product.name));	
					// MPP - Week 8 - Shop in C - Processing the Order.mov
					printf("The cost of %s in the shop is %.2f\n", c.shoppingList[a].product.name, s->stock[b].product.price);
					double subtotal = c.shoppingList[a].quantity * s->stock[b].product.price;
					printf("The cost of %d %s in the shop is %.2f\n", c.shoppingList[a].quantity, c.shoppingList[a].product.name, subtotal);
					
					s->stock[b].quantity =  s->stock[b].quantity - c.shoppingList[a].quantity;

					total = total + subtotal;

					
				}		

			}

			// If item not in shop print to screen
			if (res == 0)
					{
							printf("The shop does not have the following product: %s\n", cusItem);
					}

		
		// printf("The cost of %s in the shop is %.2f\n", c.shoppingList[i].product.name, s->stock->product.price);
		// double subtotal = c.shoppingList[i].quantity * s->stock->product.price;
		// printf("The cost of %d %s in the shop is %.2f\n", c.shoppingList[i].quantity, c.shoppingList[i].product.name, subtotal);

		// total = total + subtotal;
		
	}

	if (c.budget > total ){
	
		printf("\n-------------\n");
		printf("The total cost of %s shopping is %.2f\n", c.cname, total);
		printf("------------\n\n");

	}
	else
	{
		double insufficient_funds = total - c.budget;
		printf("\n-------------\n");
		printf("The total cost of %s shopping is %.2f\n", c.cname, total);
		printf("%s requires %.2f to pay for shopping\n", c.cname, insufficient_funds);
		printf("------------\n\n");
	}

}


// Add Menu
// https://www.studytonight.com/c/programs/misc/menu-driven-program

int main()
{
    printf("\n\n\t\tWelcome to the C Shop\n\n\n");
    int choice, num, i;
    unsigned long int fact;

	// The shop CSV should hold the initial cash value for the shop.
	// Create the Shop Stock from CSV file.
	struct Shop shop = createAndStockShop();

	struct Shop* liveShop = &shop;

    while(1)
    {
        printf("1. Stock in Shop \n");
        printf("2. Customer Shopping List\n");
        printf("3. Test  \n");
        printf("4. Exit\n\n\n");
        printf("Enter your choice :  ");
        scanf("%d",&choice);
        
        switch(choice)
        {
            case 1:
                {
				// struct Shop shop = createAndStockShop();
				// Print out Shop Stock#
				printShop(liveShop);
				}
                break;
        
            case 2:
				{
				struct Customer shoppinglist = customer_file();
				//struct Shop shop = createAndStockShop();
				printCustomer(shoppinglist, liveShop);
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