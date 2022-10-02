# Part 6
# Multiplication table for numbers up to 12


# User input integer
n = int(input("Enter number: "))

# Loop from 1 to 12
for i in range(1, 13):
    # print input the 1-12 and input multiplied by i
   print(n, 'x', i, '=', n*i)