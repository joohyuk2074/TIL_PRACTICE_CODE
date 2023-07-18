from collections import deque


def solution(maps):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n = len(maps)
    m = len(maps[0])

    data_queue = deque()
    data_queue.append((0, 0))
    maps[0][0] = 1

    while data_queue:
        x, y = data_queue.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:  # 벽이 없는 자리
                    maps[nx][ny] = maps[x][y] + 1
                    data_queue.append((nx, ny))

    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        answer = maps[n - 1][m - 1]

    return answer


input = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(input))
# input2 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
# print(solution(input2))
