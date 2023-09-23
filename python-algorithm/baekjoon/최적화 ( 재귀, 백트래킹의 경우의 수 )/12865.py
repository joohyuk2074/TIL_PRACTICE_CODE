# 평범한 배낭
def recursive(idx):
    if idx == n - 1:
        return 0

    if idx > n - 1:
        return -99999999999

    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(recursive(idx + items[idx][0]) + items[idx][1], recursive(idx + 1))
    return dp[idx]


n, k = map(int, input().split())
items = []
for _ in range(n):
    items.append(list(map(int, input().split())))
dp = [-1 for _ in range(n + 1)]

recursive(0)

print(dp)
