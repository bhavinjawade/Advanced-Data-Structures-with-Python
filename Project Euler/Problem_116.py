def Fibo(i, k):
    ways = [1] * i + [0] * (k-i+1)
    for j in range(i, k+1):
        ways[j] += ways[j - 1] + ways[j - i]
    print(ways)
    return ways[k] - 1

k = 50 
print("Number of black tiles- ", k, "units")
print("Total Number ways- ", Fibo(2, k) + Fibo(3, k) + Fibo(4, k))