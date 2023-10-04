n = int(input())
arr = list(map(int, input().split()))
print(arr)

dp = [1 for _ in range(n)]
print(dp)

for i in range(n):  # 0 1 2 3 4 5
    for j in range(i):  # i - 1 내 기준 왼쪽에 있는 숫자 까지 확인하겠다!
        if arr[i] > arr[j]:
            dp[i] = map(dp[i], dp[j] + 1)


print(max(dp))
