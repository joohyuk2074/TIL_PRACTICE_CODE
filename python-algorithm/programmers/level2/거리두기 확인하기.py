from collections import deque


def solution(places):
    answer = []

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    sol = []
    for room in places:
        queue = deque()
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    queue.append((i, j))

        find = 1
        while queue and find == 1:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and room[nx][ny] != 'X':
                    if room[nx][ny] == 'P':
                        find = 0
                        break
                    for j in range(4):
                        nnx, nny = nx + dx[j], ny + dy[j]
                        if 0 <= nnx < 5 and 0 <= nny < 5 and (x == nnx and y == nny):
                            if room[nnx][nny] == 'P':
                                find = 0
                                sol.append((nx, ny))
                                break

                    if find == 0:
                        break

        answer.append(find)
        queue.clear()

    # room = [[place[i][j] for j in range(5)] for i in range(5)]
    # checker = [[False for _ in range(5)] for _ in range(5)]
    # queue = deque()
    #
    # to_exit = False
    #
    #
    # for i in range(5):
    #     for j in range(5):
    #         if map[i][j] == 'P':  # P인 x,y 좌표를 구한다
    #             trace = []
    #
    #             queue.append((i, j))
    #             checker[i][j] = True
    #             trace.append((i, j))
    #
    #             while queue:
    #                 pair = queue.popleft()
    #                 x = pair[0]
    #                 y = pair[1]
    #                 for k in range(4):
    #                     nx = x + dx[k]
    #                     ny = y + dy[k]
    #                     if 0 <= nx < 5 and 0 <= ny < 5 and checker[nx][ny] is False:
    #                         if map[nx][ny] == 'X':
    #                             continue
    #                         elif map[nx][ny] == 'O':
    #                             queue.append((nx, ny))
    #                             checker[nx][ny] = True
    #                             trace.append((nx, ny))
    #                         elif map[nx][ny] == 'P':
    #                             if abs(i - nx) + abs(j - ny) < 2:
    #                                 to_exit = True
    #                             queue.append((nx, ny))
    #                             checker[nx][ny] = True
    #                             trace.append((nx, ny))
    #
    #             for x, y in trace:
    #                 checker[x][y] = False
    #
    # if to_exit is True:
    #     answer.append(0)
    # else:
    #     answer.append(1)
    #
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
