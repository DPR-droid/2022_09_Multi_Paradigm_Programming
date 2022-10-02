# Part 5
# Choose Sum or N

import math

# User input integer
n = int(input("Enter number: "))


print("1 - Sum of n")
print("2 - Product of n")
print("Any other key to exit")

while True: 
        choice = input("Choice: ")

        if (choice == "1"):
            sum = 0
            # loop from 1 to n
            for num in range(1, n + 1, 1):
                sum = sum + num
            print("Sum of first ", n, "numbers is: ", sum)
            break
        elif (choice == "2"):
            # Multipying by zero 
            sum = 1
            if n == 0:
                print("Product of ", n, "numbers is: 1")
            else:
               # Count backward when Multipying 
                while n > 0:
                    sum *= n
                    # reduce n by 1
                    n -= 1
                # newsum = math.factorial(n)
            print("Product of ", n, "numbers is: ", sum)
            break   
        else:
            print("Error input 1 or 2")
            break

