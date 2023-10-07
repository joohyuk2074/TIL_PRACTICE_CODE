n, x = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = n - 1

remain = 0
cnt = 0
while s <= e:
    if arr[e] == x:
        cnt += 1
        e -= 1
        continue

    if s == e:
        remain += 1

    if arr[e] + arr[s] >= x / 2:
        cnt += 1
        s += 1
        e -= 1
    else:
        s += 1
        remain += 1

print(cnt + remain // 3)
