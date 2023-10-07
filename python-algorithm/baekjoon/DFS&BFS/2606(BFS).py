from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)
    graph[end_v].append(start_v)

queue = deque()
visited[1] = 1
queue.append(1)

while queue:
    cur_v = queue.popleft()

    for v in graph[cur_v]:
        if visited[v] == 0:
            visited[v] = 1
            queue.append(v)

answer = sum(visited) - 1
print(answer)
