def recursive(x, y):
    global dp
    if dp[x][y] != 0:
        return dp[x][y]

    for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if graph[x][y] < graph[nx][ny]:
                dp[x][y] = max(dp[x][y], recursive(nx, ny) + 1)

    return dp[x][y]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        recursive(i, j)

print(max(map(max, dp)) + 1)
