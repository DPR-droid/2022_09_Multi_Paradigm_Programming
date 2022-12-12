# Multi-Paradigm Programming Shop Project 
# Build a simulation of a shop in Python OOP
# Lecturer: Dominic Carr
# Author: David Ryan

import csv
import time
import os.path
import sys


#****************************************************************
# Product class
class Product:

    # __init__ function is called every time an object is created from a class
    # price attribute is 0 if value is not applied 
    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    # returns the object representation in string format
    # def __repr__(self):
    #     #return f'PRODUCT NAME: {self.name}\nPRODUCT PRICE: €%.2f\n-------------\n\n' % self.price
    #     return self.name, self.price
        
# ProductStock class
class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    # name function attribute of class ProductStock
    def name(self):
        return self.product.name
    
    # unit_price function attribute of class ProductStock
    def unit_price(self):
        return self.product.price

    # cost function attribute of class ProductStock   
    def cost(self):
        return self.unit_price() * self.quantity

    # returns the object representation in string format  
    # def __repr__(self):
    #     return f"{self.product}The shop has {self.quantity} of:"
        
#****************************************************************


#****************************************************************
# Shop class
class Shop:
    # Create Stock from CSV file 
    def __init__(self, path):


        # Exit program if file not found
        fileexists =  os.path.exists(path)
        if fileexists == False:
            print("\nShop File not found, Exit program")
            sys.exit()

        # Read CSV file
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)
    
    # Function to print out data from Shop
    def print_shop(self):
        print(f'\n\n*******************')
        print(f'Shop has €%.2f in cash' % (self.cash))
        print(f'******************')
        for item in self.stock:
            print(f'\nThe shop has %0.0f of:' % (item.quantity))
            # print_product(item.product)
            print(f'PRODUCT NAME: {item.product.name} \nPRODUCT PRICE: €%.2f' % (item.product.price))
            print(f'-------------')

    def checkstock(custlist, shoplist):
        notinstock = set(custlist) - set(shoplist)
        # str = ""
        for nis in notinstock:
            print(f"The shop does not have the following product: {nis}")
            # str += f"The shop does not have the following product: {nis}\n"

    # def shopcash(self):
    #     return self.cash            
#****************************************************************


#****************************************************************
# Customer class
class Customer:

    def __init__(self, path):
        self.shopping_list = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.name = first_row[0]
            self.budget = float(first_row[1])
            for row in csv_reader:
                name = row[0]
                quantity = float(row[1])
                p = Product(name)
                ps = ProductStock(p, quantity)
                self.shopping_list.append(ps) 

    # Function to print customers data
    def print_customer(self):
        print(f'\n\n#### Customer Shopping List ####\n')
        print(f'Customer name is {self.name} and the budget for shopping is €%.2f' % (self.budget))
        print(f'-------------\n')

    # Function to calculate the cost of customer shopping
    def calculate_costs(self, shop):

        # Set the variable for the total cost of Customer bill.
        total = 0
        
        # Test for Quantity
        quan = 0
        
        # List for Shop and Customer Products
        custlist = []
        shoplist = []
        
        # Loop through shop products
        for shop_item in shop.stock:
            #print(f'Part 1 {shop_item.product.name}') 
            shoplist.append(shop_item.product.name)

            # Loop through customer products
            for list_item in self.shopping_list:

                #print(f'Part 2 {list_item.name()}') 
                custlist.append(list_item.name())

                # If shop and customer products match
                if (list_item.name() == shop_item.name()):
                    
                    # Get subtotal 
                    subtotal = round((shop_item.product.price * list_item.quantity),2)

                    # Know whether or not the shop can fill an order
			        # Check if shop item quantity is greater or equal customers request
                    if (shop_item.quantity >= list_item.quantity):
                        # print(shop_item.quantity )

                        # Get Total bill of shopping
                        total = total + subtotal
                    
                    # If shop item quantity is less than customer request
                    elif (shop_item.quantity < list_item.quantity):
                        print(f"The shop cannot fill the order of product: {list_item.name()}\n")
                        quan = 1

        # Shopping list that cannot be completed by the shop.
	    # Test for Quantity is set to 1 therefore thrown an appropriate error.
        if (quan == 1):
            print(f"\n-------------\n")
            print(f"Unfortunately the shop cannot fill you order\n")
            print(f"------------\n\n")
            return

        # If customer has sufficient funds
        elif (self.budget < total):
            insufficient_funds = total - self.budget
            print(f"\n-------------")
            print(f"The total cost of {self.name} shopping is €%.2f" % (total))
            print(f"{self.name} requires €%.2f more for the shopping"% (insufficient_funds))
            print(f"------------")
            return

        # Processes the orders of the customer and update the shop
        elif (self.budget >= total ):

            for shop_item in shop.stock:
            
                for list_item in self.shopping_list:

                    if (list_item.name() == shop_item.name()):
                        cusQuan = int(list_item.quantity)
                        
                        shop_item.quantity = shop_item.quantity - list_item.quantity

                        print(f'The cost of {shop_item.product.name} in the shop is €%.2f' % (shop_item.product.price))
                        subtotal = round((shop_item.product.price * list_item.quantity),2)
                        print(f'The cost of {cusQuan} {shop_item.product.name} in the shop is €%.2f\n' % subtotal)
            
            # The shop Class function of checkstock
            # Compare the list of products of shop and customer
            Shop.checkstock(custlist, shoplist)
            
            # Update the cash in the shop based on money received
            shop.cash = shop.cash + total
            print(f"\n-------------")
            print(f'The total cost of {self.name} shopping is €%.2f' % (total))

            # Output Change for Customer
            change = self.budget - total
            print(f'You have change of €%.2f' % (change))
            print(f"------------\n")

    
    def liveMode():
        # Get time
        import time
        timestr = time.strftime("%Y%m%d-%H%M%S")

        # Enter customer name
        CusName  = input("Enter Your Name : ")
        # Enter customer budget
        CusBud  = input("Enter your Budget: ")

        # Create a new filename with the customer name, time
        #  
        filename = "../" + CusName + timestr + ".csv"
        # print(filename)
        # open the file in the write mode
        # https://www.programiz.com/python-programming/csv
        with open(filename, 'w', encoding='UTF8', newline='') as f:

            writer = csv.writer(f)
            # write the header row
            writer.writerow([CusName, CusBud]) 
            print("Your name is : {} and you have €{}".format(CusName, CusBud))

            # How many Products does the customer require?
            ProdList = int(input("How many products do you have on your Shopping List: "))

            i = 0
            # Loop Through customers products and quantity
            while i < ProdList:

                pname = input("\nWhat Product do you Require? ")
                quantity = float(input("How many of {} do you require? ".format(pname)))

                # write the next row
                writer.writerow([pname, quantity])

                print(f'The product is: {pname} and you want %.0f ' % (quantity))

                i += 1
        return filename
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
    s = Shop("../stock.csv")

    while True: 
        display_menu()

        choice = input("Enter your choice :  ")

        if (choice == "1"):
            # Print out Shop Stock
            Shop.print_shop(s)
   
        elif (choice == "2"):
            # Read in original customer file
            # __init__ function is called from class Customer
            # Create a new object
            c = Customer("../customer.csv")
            # Run the function Customer print_customer            
            Customer.print_customer(c)
            # Run the function Customer calculate_costs
            c.calculate_costs(s)

        elif (choice == "3"): 
            # Customer function liveMode
            f = Customer.liveMode()
            # Create a new object
            l = Customer(f)
            # Run the function Customer print_customer  
            Customer.print_customer(l)
            # Run the function Customer calculate_costs
            l.calculate_costs(s)
            
        
        elif (choice == "4"): 
            #  User input to read in any customer orders from CSV file
            filename = input("What is the name of your shopping list? ")
            filepath = str("../" + filename)
            # Exit program if file not found
            fileexists = os.path.exists(filepath)
            # Return to main menu if file not found
            if fileexists == False:
                print("\nCustomer shopping list not found")
            else:
                c = Customer(filepath)
                Customer.print_customer(c)
                c.calculate_costs(s)

        elif (choice == "5"): 
            print("\n\n\t\t\tExit the Python OOP Shop\n")
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

    print("\n\n\t\tWelcome to the Python OOP Shop")

    main()