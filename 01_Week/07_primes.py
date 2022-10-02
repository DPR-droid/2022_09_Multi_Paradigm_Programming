# Part 7
# prints all prime numbers smaller than 100

primes = []
upto = 100

for isnumber in range(2, upto):
    isPrime = True
    # only need to check if divisable by prime
    for divisor in primes:
        # if divisable by an int it is not a prime number
        if (isnumber % divisor == 0):
            isPrime = False
            # so there is not reason to keep checking
            break

    if isPrime:
        primes.append(isnumber)

print (primes)