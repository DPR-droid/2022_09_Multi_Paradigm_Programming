import csv

class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price
    
    # def __repr__(self):
    #     #return f'PRODUCT NAME: {self.name}\nPRODUCT PRICE: €%.2f\n-------------\n\n' % self.price
    #     return self.name, self.price
        

class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def name(self):
        return self.product.name
    
    def unit_price(self):
        return self.product.price
        
    def cost(self):
        return self.unit_price() * self.quantity
        
    # def __repr__(self):
    #     return f"{self.product}The shop has {self.quantity} of:"
        


class Shop:
    
    def __init__(self, path):
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)
    

    def print_shop(self):
        print(f'\n\n*******************')
        print(f'Shop has €%.2f in cash' % (self.cash))
        print(f'******************')
        for item in self.stock:
            print(f'\nThe shop has %0.0f of:' % (item.quantity))
            # print_product(item.product)
            print(f'PRODUCT NAME: {item.product.name} \nPRODUCT PRICE: €%.2f' % (item.product.price))
            print(f'-------------')
            



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

    def print_customer(self):
        print(f'\n\n#### Customer Shopping List ####\n')
        print(f'Customer name is {self.name} and the budget for shopping is €%.2f' % (self.budget))
        print(f'-------------\n')


    def calculate_costs(self, price_list):

        quan = 0
        total = 0

        custlist = []
        shoplist = []
                
        for shop_item in price_list:
            #print(f'Part 1 {shop_item.product.name}') 
            shoplist.append(shop_item.product.name)

            for list_item in self.shopping_list:

                #print(f'Part 2 {list_item.name()}') 
                custlist.append(list_item.name())

                if (list_item.name() == shop_item.name()):


                    print(f'The cost of {shop_item.product.name} in the shop is €%.2f' % (shop_item.product.price))
                    subtotal = round((shop_item.product.price * list_item.quantity),2)
                    print(f'The cost of {list_item.quantity} {shop_item.product.name} in the shop is €%.2f\n' % subtotal)

        # print(custlist)
        # print(shoplist)

        notinstock = set(custlist) - set(shoplist)

        for nis in notinstock:
            print(f"The shop does not have the following product: {nis}")

        
    
                    
# Main
def main():

    s = Shop("../stock.csv")

    while True: 
        display_menu()

        choice = input("Enter your choice :  ")

        if (choice == "1"):
            Shop.print_shop(s)
   
        elif (choice == "2"):
            c = Customer("../customer.csv")
            Customer.print_customer(c)
            c.calculate_costs(s.stock)
            # break

        elif (choice == "3"): 
            break
        
        elif (choice == "4"): 
            filename = input("What is the name of your shopping list? ")
            filepath = str("../" + filename)
            c = Customer(filepath)
            Customer.print_customer(c)
            c.calculate_costs(s.stock)

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