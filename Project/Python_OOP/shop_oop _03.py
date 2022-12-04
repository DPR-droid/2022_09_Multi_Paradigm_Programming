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

    def shopcash(self):
        return self.cash
            



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



    def checkstock(self, custlist, shoplist):
        notinstock = set(custlist) - set(shoplist)
        str = ""
        for nis in notinstock:
            # print(f"The shop does not have the following product: {nis}")
            str += f"The shop does not have the following product: {nis}\n"

        return str


    def calculate_costs(self, shop):

        quan = 0
        total = 0

        custlist = []
        shoplist = []
                
        for shop_item in shop.stock:
            #print(f'Part 1 {shop_item.product.name}') 
            shoplist.append(shop_item.product.name)

            for list_item in self.shopping_list:

                #print(f'Part 2 {list_item.name()}') 
                custlist.append(list_item.name())

                if (list_item.name() == shop_item.name()):



                    # print(f'The cost of {shop_item.product.name} in the shop is €%.2f' % (shop_item.product.price))
                    subtotal = round((shop_item.product.price * list_item.quantity),2)
                    # print(f'The cost of {list_item.quantity} {shop_item.product.name} in the shop is €%.2f\n' % subtotal)


                    if (shop_item.quantity >= list_item.quantity):
                        # print(shop_item.quantity )

                        total = total + subtotal

                    elif (shop_item.quantity < list_item.quantity):
                        print(f"The shop cannot fill the order of product: {list_item.name()}\n")
                        quan = 1



        if (quan == 1):
            print(f"\n-------------\n")
            print(f"Unfortunately the shop cannot fill you order\n")
            print(f"------------\n\n")
            return

        elif (self.budget < total):
            insufficient_funds = total - self.budget
            print(f"\n-------------")
            print(f"The total cost of {self.name} shopping is €%.2f" % (total))
            print(f"{self.name} requires €%.2f more for the shopping"% (insufficient_funds))
            print(f"------------")
            return

        elif (self.budget >= total ):

            for shop_item in shop.stock:
            
                for list_item in self.shopping_list:

                    if (list_item.name() == shop_item.name()):
                        cusQuan = int(list_item.quantity)


                        print(f'The cost of {shop_item.product.name} in the shop is €%.2f' % (shop_item.product.price))
                        subtotal = round((shop_item.product.price * list_item.quantity),2)
                        print(f'The cost of {cusQuan} {shop_item.product.name} in the shop is €%.2f\n' % subtotal)
            
            print(self.checkstock(custlist, shoplist))

            #     for sitem in s.stock:
            #         shopItem  = sitem.product.name
            #         shopItemPrice = sitem.product.price
                    

            #         if shopItem == cusItem:
            #             sitem.quantity = sitem.quantity - citem.quantity
            #             print(f'The cost of {shopItem} in the shop is €%.2f' % (shopItemPrice))
            #             subtotal = round((shopItemPrice * cusQuan),2)
            #             print(f'The cost of {cusQuan} {cusItem} in the shop is €%.2f\n' % subtotal)

            print(f"\n-------------")
            print(f'The total cost of {self.name} shopping is €%.2f' % (total))

            change = self.budget - total
            print(f'You have change of €%.2f' % (change))
            print(f"------------\n")

            print(shop.cash)


    # https://pynative.com/python-class-method/
    @classmethod
    def liveMode(self):
        self.shopping_list_live = []
        CusName  = input("Enter Your Name : ")
        CusBud  = input("Enter your Budget: ")
        
        self.name = CusName
        self.budget = float(CusBud)
        print("Your name is : {} and you have €{}".format(CusName, CusBud))

        ProdList = int(input("How many products do you have on your Shopping List: "))

        i = 0

        while i < ProdList:


            pname = input("\nWhat Product do you Require? ")

            quantity = float(input("How many of {} do you require? ".format(pname)))

            p = Product(pname)
            ps = ProductStock(p, quantity)
            self.shopping_list_live.append(ps) 

            print(f'The product is: {pname} and you want %.0f ' % (quantity))

            i += 1
        return self.shopping_list_live


    
                    
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
            c.calculate_costs(s)

        elif (choice == "3"): 
            l = Customer.liveMode()
            print(l)
            #Customer.print_customer(l)
            
            # c.calculate_costs(s.stock)
        
        elif (choice == "4"): 
            filename = input("What is the name of your shopping list? ")
            filepath = str("../" + filename)
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