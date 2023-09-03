from collections import deque


def solution(maps):
    answer = 0

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    checks = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    flags = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    start_pair = find_x_y('S', maps)
    end_pair = find_x_y('E', maps)
    lever_pair = find_x_y('L', maps)

    q = deque()
    q.append(start_pair)
    checks[start_pair[0]][start_pair[1]] += 1
    flags[start_pair[0]][start_pair[1]] = True

    # start -> lever까지 최단 거리 구하기
    while q:
        pair = q.popleft()
        x = pair[0]
        y = pair[1]

        # lever 좌표를
        if x == lever_pair[0] and y == lever_pair[1]:
            break

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != 'X' and flags[nx][ny] is False:
                    q.append((nx, ny))
                    checks[nx][ny] = checks[x][y] + 1
                    flags[nx][ny] = True

    # lever까지 못가면 바로 -1 리턴
    if checks[lever_pair[0]][lever_pair[1]] == -1:
        return -1

    flags = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    # lever -> exit까지 최단 거리 구하기
    q.append((lever_pair[0], lever_pair[1]))
    flags[lever_pair[0]][lever_pair[1]] = True
    while q:
        pair = q.popleft()
        x = pair[0]
        y = pair[1]

        # lever 좌표를
        if x == end_pair[0] and y == end_pair[1]:
            answer = checks[x][y]
            break

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != 'X' and flags[nx][ny] is False:
                    q.append((nx, ny))
                    checks[nx][ny] = checks[x][y] + 1
                    flags[nx][ny] = True

    if checks[end_pair[0]][end_pair[1]] == -1:
        return - 1

    return answer


def find_x_y(type, maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == type:
                return i, j
    return -1, -1


maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
print(solution(maps))
