n, k = map(int, input().split())
temps = list(map(int, input().split()))

sum = 0
for i in range(0, k):
    sum += temps[i]

index = 0
answer = sum
for start_idx in range(k, n):
    sum = (sum - temps[index] + temps[start_idx])
    if answer < sum:
        answer = sum
    index += 1

print(answer)
