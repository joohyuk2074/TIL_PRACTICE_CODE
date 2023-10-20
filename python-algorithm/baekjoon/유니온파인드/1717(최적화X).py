n, m = map(int, input().split())
par = [i for i in range(n + 1)]


def _union(a, b):
    par[b] = a


def _find(a):
    if par[a] == a:
        return a
    else:
        return _find(par[a])


for _ in range(m):
    x, a, b = map(int, input().split())

    if x == 0:
        _union(a, b)
    else:
        if _find(a) == _find(b):
            print("YES")
        else:
            print("NO")
