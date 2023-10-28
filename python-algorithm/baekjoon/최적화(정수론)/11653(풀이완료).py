n = int(input())

for prime in range(2, int(n ** 0.5) + 1):
    while n % prime == 0:
        print(prime)
        n //= prime

if n > 1:
    print(n)
