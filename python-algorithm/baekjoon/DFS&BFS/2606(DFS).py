def dfs(start):
    visited[start] = 1

    for v in graph[start]:
        if visited[v] == 0:
            dfs(v)


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)
    graph[end_v].append(start_v)

dfs(1)

answer = sum(visited) - 1
print(answer)
