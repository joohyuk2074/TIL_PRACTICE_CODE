class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1

            if dp[x][y] != -1:
                return dp[x][y]

            answer = 0

            for dx, dy in [[0, 1], [1, 0]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    answer += dfs(nx, ny)

            dp[x][y] = answer
            return dp[x][y]

        return dfs(0, 0)


solution = Solution()
print(solution.uniquePaths(3, 7))
