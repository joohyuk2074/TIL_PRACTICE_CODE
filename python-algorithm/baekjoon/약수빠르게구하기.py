n = int(input())

is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i + i, n + 1, i):
            is_prime[j] = False

prime_number_set = set()
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if is_prime[i]:
            prime_number_set.add(i)

answer = []
while n != 1:
    for prime_num in prime_number_set:
        if n % prime_num == 0:
            answer.append(prime_num)
            n //= prime_num

for result in sorted(answer):
    print(result)
