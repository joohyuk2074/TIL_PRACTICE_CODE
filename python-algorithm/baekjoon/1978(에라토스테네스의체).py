n = int(input())
number_list = list(map(int, input().split()))

is_prime = [True] * 1001
is_prime[1] = False

for i in range(2, int(1001 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1001, i):
            is_prime[j] = False

answer = 0
for number in number_list:
    if is_prime[number]:
        answer += 1

print(answer)
