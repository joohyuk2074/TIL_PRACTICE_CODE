n = int(input())
answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if i + j + k == n and i != 0 and j != 0 and k != 0:
                if i % 2 == 0 and j + 2 <= k:
                    answer += 1
print(answer)
