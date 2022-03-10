
# sieve of eratosthenis
def prime(n):
    number=[0]*(n+1)
    for i in range (2, n+1):
        if number[i]==0:
            for j in range(i**2, n+1, i):
                number[j]=1

    for i in range(2, n+1):
        if number[i]==0:
            print(i, end=",")

prime(101)
