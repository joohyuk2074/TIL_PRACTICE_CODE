def recursive(index):
    if index == n:
        return 0

    if index > n:
        return -99999999999

    if dp[index] != -1:
        return dp[index]

    dp[index] = max(
        recursive(index + inputs[index][0]) + inputs[index][1],
        recursive(index + 1)
    )

    return dp[index]


n = int(input())
inputs = [list(map(int, input().split())) for _ in range(n)]
dp = [-1 for _ in range(n + 1)]

recursive(0)

print(max(dp))
