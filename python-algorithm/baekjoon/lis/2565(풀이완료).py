def lis(arr):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda x: x[0])

b_lines = [line[1] for line in lines]

length_of_lis = lis(b_lines)

print(n - length_of_lis)
