// Multi-Paradigm Programming Shop Project 
// Build a simulation of a shop in C
// Lecturer: Dominic Carr
// Author: David Ryan

//****************************************************************
// C libraries 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//****************************************************************
//  Entities
// 	- Product
// 	- ProductStock
// 	- Shop
// 	- Customer

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

//****************************************************************


//****************************************************************
// Method Print Product
// This method prints the product name and price passed from 
// struct Product

void printProduct(struct Product p)
{
	printf("PRODUCT NAME: %s \nPRODUCT PRICE: €%.2f\n", p.name, p.price);
}
//****************************************************************


//****************************************************************
// Create Stock from CSV file
// Method to import shop data from CSV file
// https://stackoverflow.com/questions/2175574/pass-path-to-file-filename-as-argument-to-a-function-that-prints-the-file-to-s
struct Shop createAndStockShop(const char* str)
{
    
	// C read file line by line
	// https://stackoverflow.com/a/3501681
	FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;


	// Exit program if file not found
    fp = fopen(str, "r");
    if (fp == NULL)
		{
		printf("\nShop File not found, Exit program\n");	
        exit(EXIT_FAILURE);
		}

	// Issue compiling in windows getline not recognised
	// To compile install WSL2 
	// https://ubuntu.com/tutorials/working-with-visual-studio-code-on-ubuntu-on-wsl2#1-overview
	// Another solution would be to manually include the function in your code which can be found 
	// at https://dev.w3.org/libwww/Library/src/vms/getline.c

	// Read file first line
	read = getline(&line, &len, fp);
	float cash = atof(line);
	// printf("cash in shop is %.2f\n", cash); // Test point
	
	// Save the value of cash to the Shop struct as the instance of 'shop'
	struct Shop shop = { cash };

    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("Retrieved line of length %zu:\n", read);  // Test point
        // printf("%s IS A LINE", line);  // Test point

		// strtok() is a string tokenization function that takes two arguments: an initial string to be parsed
		// Extract the 3 values in each line using the delimiter  
		char *n = strtok(line, ",");
		char *p = strtok(NULL, ",");
		char *q = strtok(NULL, ",");
		// atoi converts the string argument str to an integer
		int quantity = atoi(q);
		// atof converts the string argument str to a floating-point number
		double price = atof(p);
		char *name = malloc(sizeof(char) * 50);
		// strcpy copies the string pointed to, by src to dest.
		strcpy(name, n);
		// Save the value of name and price to the Product struct as the instance of 'product'
		struct Product product = { name, price };
		// Save the value of product and quantity to the ProductStock struct as the instance of 'stockItem'
		struct ProductStock stockItem = { product, quantity };
		// Index for Products
		shop.stock[shop.index++] = stockItem;
		// printf("NAME OF PRODUCT %s PRICE %.2f QUANTITY %d\n", name, price, quantity);  // Test point
    }
	
	return shop;
}

//****************************************************************
// Method to print out data from struct Shop *liveShop
// This method is reused when selecting 1 from the Menu
// The void keyword specifies that the function doesn't return a value
void printShop(struct Shop* s)
{
	// Display shop cash
	printf("\n\n*******************\n");
	printf("Shop has €%.2f in cash\n", s->cash);
	printf("******************\n");

	// Loop through shop products and print to screen the name, price, quantity
	for (int i = 0; i < s->index; i++)
	{
		printf("\nThe shop has %d of:\n", s->stock[i].quantity);
		printProduct(s->stock[i].product);
		printf("-------------\n");
	}
}
//****************************************************************

//****************************************************************
// Method to read customer CSV file from file and return
// https://stackoverflow.com/questions/2175574/pass-path-to-file-filename-as-argument-to-a-function-that-prints-the-file-to-s
// Code edited from struct Shop createAndStockShop() with reading in the firstline of csv file and get Name and Budget 
struct Customer customer_file(const char* str)
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

	// Return to main menu if file not found
    fp = fopen(str, "r");
    if (fp == NULL)
        {
		// printf("\nCustomer File not found, Test part 1\n");	  // Test point
		struct Customer custlist = {};
        return custlist;
		}
	else
		{
		// Read firstline of csv file and get Name and Budget
		read = getline(&line, &len, fp);
		char *cn = strtok(line, ",");
		char *cname = malloc(sizeof(char) * 50);
		strcpy(cname, cn);

		float budget = atof(strtok(NULL, ","));
		// printf("name %s cash for shopping is %.2f\n", name, budget);  // Test point
		
		struct Customer custlist = { cname, budget };

		while ((read = getline(&line, &len, fp)) != -1) {
			// printf("\n%s IS A LINE\n", line);  // Test point
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
}
//****************************************************************

//****************************************************************
// Method to recieve customer data from "2. Customer Shopping List" or
// "3. Live mode" or "4. File Read: Customer Shopping List"
// Read data and print results to screen
// Edited from MPP - Week 4 - Shop in C Part 2.mov

void printCustomer(struct Customer c, struct Shop* s)
{
	printf("\n\n#### Customer Shopping List ####\n\n");
	printf("Customer name is %s and the budget for shopping is €%.2f\n", c.cname, c.budget);
	printf("-------------\n\n");
	
	// Set the variable for the total cost of Customer bill.
	double total = 0;

	// Test for Quantity
	int quan = 0;

	// Loop through customer products
	for (int a = 0; a < c.index; a++)
	{
		//////////////////////////////////////////////////////////////////
		// https://www.geeksforgeeks.org/strcmp-in-c-cpp/
		// https://stackoverflow.com/questions/48133294/c-string-comparison-in-an-if-statement-doesnt-work
		// Set Check for item in shop
		int res = 0;

		//printf("The Customer wants %d of %s\n", c.shoppingList[i].quantity, c.shoppingList[i].product.name);  // Test point
		char *cusItem = c.shoppingList[a].product.name;
	
		//printf("The output 1 name is %d, for %s\n", res, cusItem);  // Test point
		// printf("The product name is  %s\n", c.shoppingList[a].product.name);  // Test point

		//////////////////////////////////////////////////////////////////
		// Edited from 
		// MPP - Week 8 - C - Passing Arguments As Pointer.mov
		// ProductStock.c
		// Loop through shop products
		for (int b = 0; b < s->index; b++)
			{

				//printf("The output 1 name is %d\n", strcmp(cusItem, s->stock[b].product.name));  // Test point

				//////////////////////////////////////////////////////////////////	
				// If shop and customer products match
				if (strcmp(s->stock[b].product.name, cusItem ) == 0)
				{
					//////////////////////////////////////////////////////////////////
					// If item in shop set res to 1
					res = 1;
					//printf("The output 2 name is %d\n", strcmp(cusItem, s->stock[b].product.name));   // Test point
					//////////////////////////////////////////////////////////////////	
					// MPP - Week 8 - Shop in C - Processing the Order.mov
					// Get subtotal 
					double subtotal = c.shoppingList[a].quantity * s->stock[b].product.price;

					
					//////////////////////////////////////////////////////////////////
					// Know whether or not the shop can fill an order
					// Check if shop item quantity is greater or equal customers request 
					if (s->stock[b].quantity >= c.shoppingList[a].quantity)
					{					
						// Get Total bill of shopping
						total = total + subtotal;
					}
					// if shop item quantity is equal to zero set res = 2
					else if (s->stock[b].quantity == 0) {
						res = 2;
						// printf("Test function 01\n");  // Test point
					}
					// If shop item quantity is less than customer request set res = 3
					else if (s->stock[b].quantity < c.shoppingList[a].quantity){
						res = 3;
						// printf("Test function 02\n");  // Test point
					}
					//////////////////////////////////////////////////////////////////
				}		

			}

			//////////////////////////////////////////////////////////////////
			// If item not in shop or cannot fill order print to screen
			// 		Thrown an appropriate error.
			if (res == 2)
					{
							printf("The shop is out of stock on the following product: %s\n", cusItem);
							// Test for Quantity set to one	
							quan = 1;					
					}
			else if (res == 3)
					{
							printf("The shop cannot fill the order of product: %s\n", cusItem);
							quan = 1;
					}
	}

	//////////////////////////////////////////////////////////////////
	// Shopping list that cannot be completed by the shop.
	// Test for Quantity is set to 1 therefore thrown an appropriate error.
	if(quan == 1){
		printf("\n-------------\n");
		printf("\nUnfortunately the shop cannot fill your order\n");
		printf("\n-------------\n");
	}
	//////////////////////////////////////////////////////////////////
	// If customer has sufficient funds	
	else if (c.budget < total){
		double insufficient_funds = total - c.budget;
		printf("\n-------------\n");
		// Print to screen the total cost of shopping and how much more the customer requires
		printf("The total cost of %s shopping is €%.2f\n", c.cname, total);
		printf("%s requires %.2f more for the shopping\n", c.cname, insufficient_funds);
		printf("------------\n\n");

	}
	//////////////////////////////////////////////////////////////////
	// Shop processes the orders of the customer
	else if (c.budget >= total ){
		for (int a = 0; a < c.index; a++)
		{
		//////////////////////////////////////////////////////////////////
		// Set Check for item in shop
		int res = 0;

		//printf("The Customer wants %d of %s\n", c.shoppingList[i].quantity, c.shoppingList[i].product.name);  // Test point

		char *cusItem = c.shoppingList[a].product.name;

		for (int b = 0; b < s->index; b++)
			{

				//printf("The output 1 name is %d\n", strcmp(cusItem, s->stock[b].product.name));  // Test point	

				// 
				if (strcmp(s->stock[b].product.name, cusItem ) == 0)
				{
					// If item in shop set res to 1
					res = 1;
					//////////////////////////////////////////////////////////////////
					// Update the Stock in the Shop
					s->stock[b].quantity =  s->stock[b].quantity - c.shoppingList[a].quantity;

					double subtotal = c.shoppingList[a].quantity * s->stock[b].product.price;

					// Print to screen the cost of the item
					printf("The cost of %s in the shop is €%.2f\n", c.shoppingList[a].product.name, s->stock[b].product.price);

					// Print to screen the total cost of the items requested by the customers
					printf("The cost of %d %s in the shop is €%.2f\n\n", c.shoppingList[a].quantity, c.shoppingList[a].product.name, subtotal);
					
				}		

			}

			//////////////////////////////////////////////////////////////////
			// If item requested by customer is not in shop 
			if (res == 0)
					{
							printf("The shop does not have the following product: %s\n", cusItem);
					}
	}	
		//////////////////////////////////////////////////////////////////
		// Update the cash in the shop based on money received
		s->cash = s->cash + total;
		printf("\n-------------\n");
		printf("The total cost of %s shopping is €%.2f\n", c.cname, total);
		//////////////////////////////////////////////////////////////////
		// Output Change for Customer
		double change = c.budget - total;
		printf("You have change of €%.2f\n", change);
		printf("------------\n\n");

	}
	

}
//****************************************************************

//****************************************************************
// Operate in a live mode, where the user can enter a product by name, specify a quantity, and pay for it. 
// The user should be able to buy many products in this way.
// https://www.programiz.com/c-programming/examples/structure-store-information
// https://programminghead.com/c-programming-printing-your-name-using-c-program

struct Customer liveMode(){
	//////////////////////////////////////////////////////////////////
	// Enter customer name
	// https://stackoverflow.com/questions/1247989/how-do-you-allow-spaces-to-be-entered-using-scanf
	char *name = malloc(sizeof(char) * 50);
	printf("Enter Your Name : "); 
	fgets(name, sizeof name, stdin);
  	scanf("%[^\n]%*c",name);

	//////////////////////////////////////////////////////////////////
	// Enter customer budget
	float budget;
	printf("Enter your Budget: ");
    scanf("%f", &budget);

	printf("Your name is : %s and you have €%.2f\n", name, budget); 
	
	struct Customer custlist2 = { name, budget };

	int i;
	int a = 0; 

	//////////////////////////////////////////////////////////////////
	// How many Products does the customer require?
	printf("How many products do you have on your Shopping List: ");
    scanf("%d", &i);
	
	//////////////////////////////////////////////////////////////////
	// Loop Through customers products and quantity
	// https://stackoverflow.com/questions/16248841/how-to-use-a-loop-function-with-user-input-in-c
	do
	{
		// Enter product name
		char *pname = malloc(sizeof(char) * 50);
		printf("\nWhat Product do you Require? "); 
		fgets(pname, sizeof pname, stdin);
  		scanf("%[^\n]%*c",pname);

		// Enter product quantity
		int quantity;
		printf("How many of %s do you require? ", pname);
		scanf("%d", &quantity);

		printf("The product is: %s and you want %d\n", pname, quantity); 
		a++;
		// printf("a is currently %d\n", a);  // Test point

		struct Product product = { pname };
		struct ProductStock stockItem = { product, quantity };
		custlist2.shoppingList[custlist2.index++] = stockItem;

	} while (a < i);
	
	return custlist2;
    
}

//****************************************************************
// Function for file path
// https://stackoverflow.com/questions/2218290/concatenate-char-array-in-c

char * filename(){
	
	
	char *filename = malloc(sizeof(char) * 50);
	printf("What is the name of your shopping list? "); 
	fgets(filename, sizeof filename, stdin);
	scanf("%s",filename);
	
	const char* path = "../";

	char* filepath;
	filepath = malloc(sizeof(char) * 50); /* make space for the new string (should check the return value ...) */
	strcpy(filepath, path); /* copy name into the new var */
	strcat(filepath, filename); /* add the extension */
	
	
	// printf("Your filename is : %s \n ", filename);   // Test point
	// printf("Your filepath is : %s \n ", filepath);   // Test point
	
	return strdup(filepath);
    
}

//****************************************************************

//****************************************************************
// https://www.studytonight.com/c/programs/misc/menu-driven-program
// Add Menu
// The option available:
// Selecting 1 - Print the Stock and Cash avaiable to the shop 

// Selecting 2 - Read in customer orders from original CSV file 'customer.csv'.
// – That file should include all the products they want and the quantity.
// – It should also include their name and budget
// - Process the orders of the customer
// - Know whether or not the shop can fill an order
// - Thrown an appropriate error.
// - 

// Selecting 3 - Operate in a live mode, where the user can enter a 
// product by name, specify a quantity, and pay for it. 
// The user should be able to buy many products in this way.
// – It should also include their name and budget
// - Process the orders of the customer
// - Know whether or not the shop can fill an order
// - Thrown an appropriate error.

// Selecting 4 - User can input CSV filename from file location '../'
// – That file should include all the products they want and the quantity.
// – It should also include their name and budget
// - Process the orders of the customer
// - Know whether or not the shop can fill an order
// - Thrown an appropriate error.
// - 

// Selecting 5 - Exit the Program.

int main()
{
    printf("\n\n\t\tWelcome to the C Proc Shop\n");
    int choice, num, i;
    unsigned long int fact;

	// The shop CSV should hold the initial cash value for the shop.
	// Create the Shop Stock from CSV file.
	struct Shop shop = createAndStockShop("../stock.csv");
	// Create a live copy of the shop
	struct Shop* liveShop = &shop;

    while(1)
    {
        // Print user menu
		printf("\n\n#### Main Menu ####\n");
		printf("1. Stock in Shop\n");
        printf("2. Customer Shopping List\n");
        printf("3. Live mode\n");
		printf("4. File Read: Customer Shopping List\n");
        printf("5. Exit\n\n\n");
        printf("Enter your choice :  ");
        scanf("%d",&choice);
        
        switch(choice)
        {
            case 1:
                {
				// struct Shop shop = createAndStockShop();
				// Print out Shop Stock
				printShop(liveShop);
				}
                break;
        
            case 2:
				{
				// Read in original customer file
				struct Customer shoppinglist = customer_file("../customer.csv");
				printCustomer(shoppinglist, liveShop);
				}
                break;
        
            case 3:
				{
				// Live Mode
				struct Customer shoppinglist2 = liveMode();
				printCustomer(shoppinglist2, liveShop);
				}
				break;
			
			case 4:
				{
				// User input to read in any customer orders from CSV file
				char* userfile = filename();
				// printf("Your filepath is : %s \n ", userfile);  // Test point
				struct Customer shoppinglist3 = customer_file(userfile);
				// printf("Customer name is %s and the budget for shopping is €%.2f\n", shoppinglist.cname, shoppinglist.budget);  // Test point
				// Verify if struct is empty
				if (shoppinglist3.cname == NULL )
					{
					printf("\nCustomer shopping list not found\n");
					}
				else
					{
					printCustomer(shoppinglist3, liveShop);
					}
				}
				break;
        
            case 5:
                printf("\n\n\t\t\tExit the C Proc Shop\n\n\n");
                exit(0);    // terminates the complete program execution
        }
    }
    printf("\n\n\t\t\tCoding in C is Fun!\n\n\n");
    return 0;
}
//////////////////////////////////////////////////////////////////