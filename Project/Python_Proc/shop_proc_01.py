from dataclasses import dataclass, field
from typing import List
import csv

@dataclass
class Product:
    name: str
    price: float = 0.0

@dataclass 
class ProductStock:
    product: Product
    quantity: int

@dataclass 
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str = ""
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

def create_and_stock_shop():
    s = Shop()
    with open('../stock.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        first_row = next(csv_reader)
        s.cash = float(first_row[0])
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            #print(ps)
    return s
    
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
        print("****************************")
        # print(c)
        return c 
        

def print_product(p):
    print(f'\nPRODUCT NAME: {p.name} \nPRODUCT PRICE: {p.price}')
    return p.name, p.price

def print_customer(c, s):
    print(f'CUSTOMER NAME: {c.name} \nCUSTOMER BUDGET: {c.budget}')

    quan = 0
    total = 0
    
    for citem in c.shopping_list:
        #cusItem, cusprice = print_product(citem.product)
        cusItem = citem.product.name
        cusQuan = int(citem.quantity)
        
        
        for sitem in s.stock:
            shopItem  = sitem.product.name
            shopItemPrice = sitem.product.price
            if shopItem == cusItem:
                print(f'The cost of {shopItem} in the shop is {shopItemPrice}')
                subtotal = round((shopItemPrice * cusQuan),2)
                print(f'The cost of {cusQuan} {cusItem} in the shop is %.2f\n' % subtotal)

                if (sitem.quantity >= citem.quantity):
                    # print(sitem.quantity)

                    total = total + subtotal

                elif (sitem.quantity == 0):
                    print(f"The shop does not have the following product:{cusItem}\n")
                    # print("Test 1")
                    quan = 1

                elif (sitem.quantity < citem.quantity):
                    print(f"The shop cannot fill the order of product: {cusItem}\n")
                    # print("Test 2")
                    quan = 1
            
            # elif shopItem != cusItem:
            #     print(f"The shop does not have the following product:{cusItem}\n")

       

    if (c.budget < total):
        insufficient_funds = total - c.budget
        print(f"\n-------------\n")
        print(f"The total cost of {c.name} shopping is {total}\n\n")
        print(f"{c.name} requires {insufficient_funds} more for the shopping\n")
        print(f"------------\n\n")

    elif (quan == 1):
        print(f"\n-------------\n")
        print(f"Unfortunately the shop cannot fill you order\n")
        print(f"------------\n\n")

    elif (c.budget >= total ):
        print(f"\n-------------\n")
        print(f"The total cost of {c.name} shopping is {total}\n\n")

        change = c.budget - total
        print(f"You have change of ???{change}\n")
        print(f"------------\n\n")


        
def print_shop(s):
    print(f'Shop has {s.cash} in cash')
    for item in s.stock:
        print_product(item.product)
        print(f'The Shop has {item.quantity} of the above')

# s = create_and_stock_shop()
# print_shop(s)


# Main
def main():

    s = create_and_stock_shop()

    while True: 
        display_menu()

        choice = input("Choice: ")
        # 
        if (choice == "1"):
            
            print_shop(s)
            # break
            
        # 
        elif (choice == "2"):
            c = read_customer("../customer.csv")
            print_customer(c, s)

            # break

        elif (choice == "3"): 
            
            break

        elif (choice == "4"): 
            
            break

        else:
            # If user does not choose the correct input
            # Print a message to the screen 
            # Returns user to main menu 
            print("\n***Please choose a number from above list or to exit press 4***\n")

# Displays a main menu for User
def display_menu():
    print("\n\n#### Main Menu ####\n")
    print("1. Stock in Shop ")
    print("2. Customer Shopping List")
    print("3. Live mode")
    print("4. Exit")


if __name__ == "__main__":
    main()