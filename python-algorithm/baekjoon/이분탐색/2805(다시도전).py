n, m = map(int, input().split())
forest = list(map(int, input().split()))

s = 1
e = max(forest)

while s <= e:
    mid = (s + e) // 2

    wood = 0
    for tree in forest:
        if tree >= mid:
            wood += (tree - mid)

    if wood >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)
