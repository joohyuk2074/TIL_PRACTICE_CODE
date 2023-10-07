M = list(str(input()))
N = list(str(input()))

dp = [[0 for _ in range(len(N) + 1)] for _ in range(len(M) + 1)]

for i in range(1, len(M) + 1):  # 문자열 하나 결정
    for j in range(1, len(N) + 1):  # 문자를 결정
        if M[i - 1] == N[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


print(dp[len(M)][len(N)])