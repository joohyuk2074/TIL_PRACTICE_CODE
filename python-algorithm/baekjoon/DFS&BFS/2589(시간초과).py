from collections import deque


def get_max_num(dist):
    max_result = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if max_result < dist[i][j]:
                max_result = dist[i][j]
    return max_result


n, m = map(int, input().split())
graph = []
for _ in range(n):
    line = input()
    graph.append(list(line))

start = tuple()
end = tuple()

# 보물 뭍기
max_dist = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            visited = [[0 for _ in range(m)] for _ in range(n)]
            dist = [[0 for _ in range(m)] for _ in range(n)]

            queue = deque()
            queue.append((i, j))
            visited[i][j] = 1

            while queue:
                x, y = queue.popleft()

                for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == "L" and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            dist[nx][ny] = dist[x][y] + 1
                            max_dist = max(max_dist, dist[nx][ny])
                            queue.append((nx, ny))

print(max_dist)
