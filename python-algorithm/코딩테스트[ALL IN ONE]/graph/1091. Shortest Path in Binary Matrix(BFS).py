from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        def bfs(x, y):
            dx = [-1, -1, -1, 0, 1, 1, 1, 0]
            dy = [-1, 0, 1, 1, 1, 0, -1, -1]

            queue = deque()

            queue.append((x, y))
            dp[x][y] = 1

            while queue:
                cx, cy = queue.popleft()

                for i in range(0, 8):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 0 and dp[nx][ny] == 0:
                            dp[nx][ny] = dp[cx][cy] + 1
                            queue.append((nx, ny))

        if grid[0][0] == 1:
            return -1

        bfs(0, 0)

        answer = dp[n - 1][n - 1]
        if answer == 0:
            return -1

        return answer


solution = Solution()

grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(solution.shortestPathBinaryMatrix(grid))

grid1 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
print(solution.shortestPathBinaryMatrix(grid1))
