from collections import deque


def solution(maps):
    answer = []

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    matrix = [list(text) for text in maps]
    row_length = len(maps)
    column_length = len(maps[0])
    flag_map = [[False for _ in range(column_length)] for _ in range(row_length)]

    queue = deque()
    for x in range(row_length):
        for y in range(column_length):
            if maps[x][y] != 'X' and flag_map[x][y] is False:
                queue.append((x, y))
                flag_map[x][y] = True
                sum = int(matrix[x][y])

                while queue:
                    coordinate = queue.popleft()
                    cx = coordinate[0]
                    cy = coordinate[1]
                    for i in range(4):

                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if 0 <= nx < row_length and 0 <= ny < column_length:
                            if matrix[nx][ny] != 'X' and flag_map[nx][ny] is False:
                                flag_map[nx][ny] = True
                                queue.append((nx, ny))
                                sum += int(matrix[nx][ny])

                answer.append(sum)

    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return sorted(answer)


maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
print(solution(maps))

maps2 = ["XXX", "XXX", "XXX"]
print(solution(maps2))
