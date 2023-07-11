n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    start = array[i]
    for j in range(start, m + 1):
        if d[j - start] != 10001:
            d[j] = min(d[j], d[j - start] + 1)
