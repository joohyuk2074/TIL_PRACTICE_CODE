from collections import deque


class Solution:
    def numIslands(self, grid):
        queue = deque()
        checking_map = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        row_length = len(grid)
        column_length = len(grid[0])

        answer = 0
        for x in range(row_length):
            for y in range(column_length):
                if grid[x][y] == "1" and checking_map[x][y] is False:
                    checking_map[x][y] = True
                    queue.append((x, y))

                    while queue:
                        cx, cy = queue.popleft()
                        for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                            nx = cx + dx
                            ny = cy + dy
                            if 0 <= nx < row_length and 0 <= ny < column_length:
                                if grid[nx][ny] == "1" and checking_map[nx][ny] is False:
                                    checking_map[nx][ny] = True
                                    queue.append((nx, ny))
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
