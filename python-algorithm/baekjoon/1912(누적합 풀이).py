# 누적합 풀이
n = int(input())
number_list = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = max(prefix[i] + number_list[i], number_list[i])

print(max(prefix))
