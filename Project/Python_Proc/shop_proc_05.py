from dataclasses import dataclass, field
from typing import List
import csv

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

def create_and_stock_shop(file_path):
    s = Shop()
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
        

def print_product(p):
    print(f'PRODUCT NAME: {p.name} \nPRODUCT PRICE: €%.2f' % (p.price))
    return p.name, p.price

def print_customer(c, s):
    print(f'\n\n#### Customer Shopping List ####\n')
    print(f'Customer name is {c.name} and the budget for shopping is €%.2f' % (c.budget))
    print(f'-------------\n')

    quan = 0
    total = 0
   
    custlist = []
    shoplist = []
    

    for citem in c.shopping_list:
        cusItem = citem.product.name
        cusQuan = int(citem.quantity)

        custlist.append(cusItem)
                
        
        for sitem in s.stock:
            shopItem  = sitem.product.name
            shopItemPrice = sitem.product.price
        
            if shopItem == cusItem:
                
                subtotal = round((shopItemPrice * cusQuan),2)

                shoplist.append(shopItem)

                if (sitem.quantity >= citem.quantity):

                    total = total + subtotal

                # elif (sitem.quantity == 0):
                #     print(f"The shop does not have the following product:{cusItem}\n")
                #     quan = 1

                elif (sitem.quantity < citem.quantity):
                    print(f"The shop cannot fill the order of product: {cusItem}\n")
                    quan = 1
            

     
    notinstock = set(custlist) - set(shoplist)
   

    if (quan == 1):
        print(f"\n-------------\n")
        print(f"Unfortunately the shop cannot fill you order\n")
        print(f"------------\n\n")
        return

    elif (c.budget < total):
        insufficient_funds = total - c.budget
        print(f"\n-------------")
        print(f"The total cost of {c.name} shopping is €%.2f" % (total))
        print(f"{c.name} requires €%.2f more for the shopping"% (insufficient_funds))
        print(f"------------")
        return

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

        for nis in notinstock:
            print(f"The shop does not have the following product: {nis}")

        s.cash = s.cash + total
        # print(s.cash)
        print(f"\n-------------")
        print(f'The total cost of {c.name} shopping is €%.2f' % (total))

        change = c.budget - total
        print(f'You have change of €%.2f' % (change))
        print(f"------------\n")


        
def print_shop(s):
    print(f'\n\n*******************')
    print(f'Shop has €%.2f in cash' % (s.cash))
    print(f'******************')
    for item in s.stock:
        print(f'\nThe shop has %0.0f of:' % (item.quantity))
        print_product(item.product)
        print(f'-------------')
        

def liveMode():
    CusName  = input("Enter Your Name : ")
    CusBud  = input("Enter your Budget: ")
    


    print("Your name is : {} and you have €{}".format(CusName, CusBud)); 

    c = Customer(CusName, float(CusBud))

    ProdList = int(input("How many products do you have on your Shopping List: "))

    i = 0

    while i < ProdList:


        pname = input("\nWhat Product do you Require? ")

        quantity = float(input("How many of {} do you require? ".format(pname)))

        p = Product(pname)
        ps = ProductStock(p, quantity)
        c.shopping_list.append(ps)

        print(f'The product is: {pname} and you want %.0f ' % (quantity))

        i += 1

    return c


# Main
def main():

    s = create_and_stock_shop('../stock.csv')

    while True: 
        display_menu()

        choice = input("Enter your choice :  ")
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
            c = liveMode()
            print_customer(c, s)
            # break
        
        elif (choice == "4"): 
            filename = input("What is the name of your shopping list? ")
            filepath = str("../" + filename)
            # print(filepath)
            c = read_customer(filepath)
            print_customer(c, s)
            # break

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