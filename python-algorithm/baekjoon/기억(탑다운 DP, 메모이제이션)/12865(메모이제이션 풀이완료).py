def recursive(index, weight):
    if weight > k:
        return -999999999

    if index == n:
        return 0

    if dp[index][weight] != -1:
        return dp[index][weight]

    dp[index][weight] = max(
        recursive(index + 1, weight + inputs[index][0]) + inputs[index][1],
        recursive(index + 1, weight)
    )

    return dp[index][weight]


n, k = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100_001)] for _ in range(n)]

print(recursive(0, 0))
