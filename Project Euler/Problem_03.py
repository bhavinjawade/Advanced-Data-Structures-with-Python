def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
n =  600851475143
facs = prime_factors(n)
print(facs)
print("root n is " + str(n**(1/2)))