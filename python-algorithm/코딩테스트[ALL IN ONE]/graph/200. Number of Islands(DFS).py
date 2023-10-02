class Solution:
    def dfs(self, x, y, grid, checking_map):
        checking_map[x][y] = True

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == "1" and checking_map[nx][ny] is False:
                    self.dfs(nx, ny, grid, checking_map)

    def numIslands(self, grid):
        checking_map = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        answer = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and checking_map[x][y] is False:
                    self.dfs(x, y, grid, checking_map)
                    answer += 1

        return answer


solution = Solution()

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(solution.numIslands(grid))
