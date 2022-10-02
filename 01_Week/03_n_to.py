# Part 3
# To the N

# User input integer
n = int(input("Enter number: "))

# Set sum to zero
sum = 0
# Loop from 1 to n
for num in range(1, n + 1, 1):
    # add num to sum
    sum = sum + num

# prints the sum of the numbers 1 to n 
print("Sum of", n, "is:", sum)