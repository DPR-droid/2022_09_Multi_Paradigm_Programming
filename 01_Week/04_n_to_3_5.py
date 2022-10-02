# Part 4
# To the N only with Multiples of 3 & 5

# n = 17
# User input integer
n = int(input("Enter number: "))

sum = 0

# Loop from 1 to n
for num in range(1, n + 1, 1):
    # only need to check if divisable by 5 or 3
    if (num % 5) == 0 or (num % 3) == 0:
        # print(num)
        sum = sum + num
# prints the sum of the numbers 1 to n 
print("Sum of", n, "is:", sum)