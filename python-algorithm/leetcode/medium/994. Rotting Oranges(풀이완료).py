from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        checked = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = deque()

        # 첫 썩은 사과 x, y값 및 day를 큐에 삽입
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        while queue:
            info = queue.popleft()
            x = info[0]
            y = info[1]
            day = info[2]

            for dx, dy in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1 and checked[nx][ny] == 0:
                        grid[nx][ny] = 2
                        checked[nx][ny] = day + 1
                        queue.append((nx, ny, day + 1))

        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

                if answer < checked[i][j]:
                    answer = checked[i][j]
        return answer


solution = Solution()
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(solution.orangesRotting(grid))
