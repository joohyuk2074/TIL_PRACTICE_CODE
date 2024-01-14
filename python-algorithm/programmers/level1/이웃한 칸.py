def solution(board, h, w):
    n = len(board)
    count = 0

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(0, 4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0 <= nh < n and 0 <= nw < n:
            if board[h][w] == board[nh][nw]:
                count += 1

    return count


board = [["blue", "red", "orange", "red"],
         ["red", "red", "blue", "orange"],
         ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]]

h = 1
w = 1

result = solution(board, 1, 1)
print(result)
