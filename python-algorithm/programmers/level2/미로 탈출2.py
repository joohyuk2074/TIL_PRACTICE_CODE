from collections import deque

def solution(maps):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    def bfs(start, end, maps):
        checks = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
        flags = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
        q = deque([start])
        checks[start[0]][start[1]] = 0
        flags[start[0]][start[1]] = True

        while q:
            x, y = q.popleft()

            if x == end[0] and y == end[1]:
                return checks[x][y]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] != 'X' and not flags[nx][ny]:
                        q.append((nx, ny))
                        checks[nx][ny] = checks[x][y] + 1
                        flags[nx][ny] = True

        return -1

    start_pair = find_x_y('S', maps)
    end_pair = find_x_y('E', maps)
    lever_pair = find_x_y('L', maps)

    distance_to_lever = bfs(start_pair, lever_pair, maps)
    if distance_to_lever == -1:
        return -1

    distance_to_exit = bfs(lever_pair, end_pair, maps)
    if distance_to_exit == -1:
        return -1

    return distance_to_lever + distance_to_exit

def find_x_y(type, maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == type:
                return (i, j)
    return -1, -1

maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
print(solution(maps))  # Expected output is the correct value
