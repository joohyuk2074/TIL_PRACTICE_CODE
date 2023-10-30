n = int(input())
temps = list(map(int, input().split()))

dp = [0] * n
dp[0] = temps[0]
for i in range(1, n):
    dp[i] = temps[i]
    if dp[i] < dp[i - 1] + temps[i]:
        dp[i] = dp[i - 1] + temps[i]

answer = max(dp)
print(answer)
