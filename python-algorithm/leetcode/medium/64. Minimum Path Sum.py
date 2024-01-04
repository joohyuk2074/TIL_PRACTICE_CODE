class Solution:
    def minPathSum(self, grid):
        m_length = len(grid)
        n_length = len(grid[0])
        dp = [[0 for _ in range(n_length)] for _ in range(m_length)]

        # 가로
        for i in range(n_length):
            if i == 0:
                dp[0][0] = grid[0][0]
            else:
                dp[0][i] = dp[0][i - 1] + grid[0][i]

        # 세로
        for i in range(1, m_length):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m_length):
            for j in range(1, n_length):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m_length - 1][n_length - 1]


solution = Solution()
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
path_sum = solution.minPathSum(grid)
print(path_sum)
