from collections import deque


def solution(board):
    answer = 100000

    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_x = i
                start_y = j
            if board[i][j] == 'G':
                end_x = i
                end_y = j

    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    count = 0
    while queue:

        pair = queue.popleft()
        cx = pair[0]
        cy = pair[1]

        if board[cx][cy] == 'G':
            answer = min(answer, count)
            continue

        for i in range(0, 4):
            x = cx + dx[i]
            y = cy + dy[i]

            if 0 > x or x >= len(board) or 0 > y or y >= len(board[0]):
                continue

            if board[x][y] == 'D':
                continue

            while 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != 'D':
                x += dx[i]
                y += dy[i]

            x -= dx[i]
            y -= dy[i]

            if visited[x][y]:
                continue

            visited[x][y] = True
            queue.append((x, y))
            count += 1

    answer = count
    return answer


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))
