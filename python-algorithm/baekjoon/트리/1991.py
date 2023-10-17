n = int(input())
graph = [[] for _ in range(n + 1)]
par = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def recursive(node, prev):
    par[node] = prev

    for nxt in graph[node]:
        if nxt == prev:
            continue
        recursive(nxt, node)


recursive(1, 0)


for i in range(1, len(par)):
    print(par[i])