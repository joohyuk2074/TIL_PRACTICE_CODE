import sys


def find(x):
    # 경로 압축 기법
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x


# 입력 받기
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())

    if op == 0:  # Union 연산
        union(a, b)
    else:  # Find 연산
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
