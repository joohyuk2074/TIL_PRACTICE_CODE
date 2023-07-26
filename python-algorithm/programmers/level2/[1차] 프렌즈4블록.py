def solution(m, n, board):
    answer = 0

    # 2차원 배열로 세팅
    game_map = [['' for _ in range(n)] for _ in range(m)]
    flag_set = set()
    for i in range(m):
        for j in range(n):
            game_map[i][j] = board[i][j]

    # for row in range(m - 1):
        # print(game_map)
    while True:
        isDeleted = False
        for i in range(0, m - 1):
            for j in range(n - 1):
                c = game_map[i][j]
                right_c = game_map[i][j + 1]
                down_c = game_map[i + 1][j]
                diagonal_c = game_map[i + 1][j + 1]
                if c != '' and (c == right_c == down_c == diagonal_c):
                    flag_set.add((i, j))
                    flag_set.add((i, j + 1))
                    flag_set.add((i + 1, j))
                    flag_set.add((i + 1, j + 1))
                    isDeleted = True

        # 저장된 set의 좌표를 꺼내서 빈 문자열로 세팅
        while flag_set:
            pop = flag_set.pop()
            # print(pop[0], pop[1])
            game_map[pop[0]][pop[1]] = ''
            answer += 1

        # print(game_map)

        for column in range(n):
            queue = []
            for i in range(m):
                if game_map[i][column] != '':
                    queue.append(game_map[i][column])

            for i in range(m - 1, -1, -1):
                if queue:
                    game_map[i][column] = queue.pop()
                else:
                    game_map[i][column] = ''
        # print(game_map)
        if isDeleted is False:
            break

    return answer


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))
# m1 = 7
# n1 = 2
# board2 = ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]
# print(solution(m1, n1, board2))
