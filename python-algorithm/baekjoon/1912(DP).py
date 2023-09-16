n = int(input())
number_list = list(map(int, input().split()))

dp = [0] * n
dp[0] = number_list[0]
for i in range(1, n):
    dp[i] = number_list[i]
    if dp[i] < dp[i - 1] + number_list[i]:
        dp[i] = dp[i - 1] + number_list[i]

answer = -1 * 1001
for i in range(n):
    if answer < dp[i]:
        answer = dp[i]

print(answer)
