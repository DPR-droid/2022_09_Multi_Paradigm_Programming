# Multi-Paradigm Programming Shop Project 
# Build a simulation of a shop in Python Procedural
# Lecturer: Dominic Carr
# Author: David Ryan


from dataclasses import dataclass, field
from typing import List
import csv
import os.path
import sys


#****************************************************************
#  Entities
# 	- Product
# 	- ProductStock
# 	- Shop
# 	- Customer


# What is a dataclass?
# https://www.pythoncheatsheet.org/cheatsheet/dataclasses
# They store data and represent a certain data type. It represents a specific kind of entity. It holds attributes that define or represent the entity. 
# They can be compared to other objects of the same type. Ex: A number can be greater than, less than, or equal to another number.
@dataclass
class Product:
    name: str
    price: float = 0.00

@dataclass 
class ProductStock:
    product: Product
    quantity: int

@dataclass 
class Shop:
    cash: float = 0.00
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.00
    shopping_list: List[ProductStock] = field(default_factory=list)

#****************************************************************


#****************************************************************
# Function Print Product
# This function prints the product name and price

def print_product(p):
    print(f'PRODUCT NAME: {p.name} \nPRODUCT PRICE: €%.2f' % (p.price))
    return p.name, p.price
#****************************************************************


#****************************************************************
# Create Stock from CSV file
# Function to import shop data from CSV file
def create_and_stock_shop(file_path):
    
    # Intializing the Shop dataclass.
    s = Shop()

    # Exit program if file not found
    fileexists =  os.path.exists(file_path)
    if fileexists == False:
        print("\nShop File not found, Exit program")
        sys.exit()

    # Read CSV file
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        s.cash = float(first_row[0])
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            #print(ps)
    return s
#****************************************************************


#****************************************************************
# Function to print out data from Shop
# This function is reused when selecting 1 from the Menu
#****************************************************************
def print_shop(s):
    print(f'\n\n*******************')
    print(f'Shop has €%.2f in cash' % (s.cash))
    print(f'******************')
    for item in s.stock:
        print(f'\nThe shop has %0.0f of:' % (item.quantity))
        print_product(item.product)
        print(f'-------------')
#****************************************************************


#****************************************************************
# Create Stock from CSV file
# Function to import customer data from CSV file
def read_customer(file_path):

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            c = Customer(first_row[0], float(first_row[1]))
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                c.shopping_list.append(ps)
            return c 
 #****************************************************************


#****************************************************************
# Function to recieve customer data from "2. Customer Shopping List" or
# "3. Live mode" or "4. File Read: Customer Shopping List"
# Read data and print results to screen
def print_customer(c, s):
    print(f'\n\n#### Customer Shopping List ####\n')
    print(f'Customer name is {c.name} and the budget for shopping is €%.2f' % (c.budget))
    print(f'-------------\n')

    # Set the variable for the total cost of Customer bill.
    total = 0
    
    # Test for Quantity
    quan = 0
    
    # List for Shop and Customer Products
    custlist = []
    shoplist = []
    
    # Loop through customer products
    for citem in c.shopping_list:
        cusItem = citem.product.name
        cusQuan = int(citem.quantity)

        # Add to customer product list
        custlist.append(cusItem)
                
        # Loop through shop products
        for sitem in s.stock:
            shopItem  = sitem.product.name
            shopItemPrice = sitem.product.price

            # If shop and customer products match
            if shopItem == cusItem:
                
                # Get subtotal 
                subtotal = round((shopItemPrice * cusQuan),2)
                # Add to shop product list
                shoplist.append(shopItem)

                # Know whether or not the shop can fill an order
			    # Check if shop item quantity is greater or equal customers request 
                if (sitem.quantity >= citem.quantity):

                    # Get Total bill of shopping
                    total = total + subtotal

                # If shop item quantity is less than customer request
                elif (sitem.quantity < citem.quantity):
                    print(f"The shop cannot fill the order of product: {cusItem}\n")
                    quan = 1
            

    # Compare the list of products of shop and customer
    # https://www.codingem.com/difference-between-two-python-lists/
    notinstock = set(custlist) - set(shoplist)
   
    # Shopping list that cannot be completed by the shop.
	# Test for Quantity is set to 1 therefore thrown an appropriate error.
    if (quan == 1):
        print(f"\n-------------\n")
        print(f"Unfortunately the shop cannot fill you order\n")
        print(f"------------\n\n")
        return

    # If customer has sufficient funds	
    elif (c.budget < total):
        insufficient_funds = total - c.budget
        print(f"\n-------------")
        print(f"The total cost of {c.name} shopping is €%.2f" % (total))
        print(f"{c.name} requires €%.2f more for the shopping"% (insufficient_funds))
        print(f"------------")
        return

    # Shop processes the orders of the customer
    elif (c.budget >= total ):

        for citem in c.shopping_list:
            #cusItem, cusprice = print_product(citem.product)
            cusItem = citem.product.name
            cusQuan = int(citem.quantity)
        
        
            for sitem in s.stock:
                shopItem  = sitem.product.name
                shopItemPrice = sitem.product.price
                

                if shopItem == cusItem:
                    sitem.quantity = sitem.quantity - citem.quantity
                    print(f'The cost of {shopItem} in the shop is €%.2f' % (shopItemPrice))
                    subtotal = round((shopItemPrice * cusQuan),2)
                    print(f'The cost of {cusQuan} {cusItem} in the shop is €%.2f\n' % subtotal)

        # If item requested by customer is not in shop 
        for nis in notinstock:
            print(f"The shop does not have the following product: {nis}")

        # Update the cash in the shop based on money received
        s.cash = s.cash + total
        # print(s.cash)
        print(f"\n-------------")
        print(f'The total cost of {c.name} shopping is €%.2f' % (total))

        # Output Change for Customer
        change = c.budget - total
        print(f'You have change of €%.2f' % (change))
        print(f"------------\n")
#****************************************************************
#****************************************************************
# Operate in a live mode, where the user can enter a product by name, specify a quantity, and pay for it. 
# The user should be able to buy many products in this way.
def liveMode():
    # Enter customer name
    CusName  = input("Enter Your Name : ")
    # Enter customer budget
    CusBud  = input("Enter your Budget: ")
    
    print("Your name is : {} and you have €{}".format(CusName, CusBud))

    c = Customer(CusName, float(CusBud))

    # How many Products does the customer require?
    ProdList = int(input("How many products do you have on your Shopping List: "))

    i = 0

    # Loop Through customers products and quantity
    while i < ProdList:

        pname = input("\nWhat Product do you Require? ")

        quantity = float(input("How many of {} do you require? ".format(pname)))

        p = Product(pname)
        ps = ProductStock(p, quantity)
        c.shopping_list.append(ps)

        print(f'The product is: {pname} and you want %.0f ' % (quantity))

        i += 1

    return c
#****************************************************************


#****************************************************************
# Main
# Add Menu
# The option available:
# Selecting 1 - Print the Stock and Cash avaiable to the shop 

# Selecting 2 - Read in customer orders from original CSV file 'customer.csv'.
# – That file should include all the products they want and the quantity.
# – It should also include their name and budget
# - Process the orders of the customer
# - Know whether or not the shop can fill an order
# - Thrown an appropriate error.
# - 

# Selecting 3 - Operate in a live mode, where the user can enter a 
# product by name, specify a quantity, and pay for it. 
# The user should be able to buy many products in this way.
# – It should also include their name and budget
# - Process the orders of the customer
# - Know whether or not the shop can fill an order
# - Thrown an appropriate error.

# Selecting 4 - User can input CSV filename from file location '../'
# – That file should include all the products they want and the quantity.
# – It should also include their name and budget
# - Process the orders of the customer
# - Know whether or not the shop can fill an order
# - Thrown an appropriate error.
# - 

# Selecting 5 - Exit the Program.

def main():

    # The shop CSV should hold the initial cash value for the shop.
    # Create the Shop Stock from CSV file.
    s = create_and_stock_shop('../stock.csv')

    while True: 
        display_menu()

        choice = input("Enter your choice :  ")

        if (choice == "1"):
            # Print out Shop Stock
            print_shop(s)

        elif (choice == "2"):
            # Read in original customer file
            # Create a new object
            c = read_customer("../customer.csv")
            # Call function to print customer details and process the order
            print_customer(c, s)

        elif (choice == "3"): 
            # Live Mode
            # Create a new object
            c = liveMode()
            # Call method to print customer details and process the order 
            print_customer(c, s)
        
        elif (choice == "4"): 
            #  User input to read in any customer orders from CSV file
            filename = input("What is the name of your shopping list? ")
            filepath = str("../" + filename)
            # Return to main menu if file not found
            fileexists = os.path.exists(filepath)
            if fileexists == False:
                print("\nCustomer shopping list not found")
            else:
                c = read_customer(filepath)
                # Call function to print customer details and process the order
                print_customer(c, s)

        elif (choice == "5"): 
            print("\n\n\t\t\tExit the Python Proc Shop\n")
            break

        else:
            # If user does not choose the correct input
            # Print a message to the screen 
            # Returns user to main menu 
            print("\n***Please choose a number from above list or to exit press 5***\n")

# Displays a main menu for User
def display_menu():
    print("\n\n#### Main Menu ####")
    print("1. Stock in Shop ")
    print("2. Customer Shopping List")
    print("3. Live mode")
    print("4. File Read: Customer Shopping List")
    print("5. Exit\n\n")


if __name__ == "__main__":

    print("\n\n\t\tWelcome to the Python Proc Shop")

    main()