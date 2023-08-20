def solution(rows, columns, queries):
    answer = []

    # 1. 행렬 생성
    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    # 2. 행렬 테두리 회전
    for x1, y1, x2, y2 in queries:
        min_num = rows * columns

        start_x = x1 - 1
        start_y = y1 - 1
        end_x = x2 - 1
        end_y = y2 - 1

        temp1 = matrix[start_x][end_y]
        for j in range(end_y, start_y, -1):
            matrix[start_x][j] = matrix[start_x][j - 1]
            num = matrix[start_x][j]
            if min_num > num:
                min_num = num

        temp2 = matrix[end_x][end_y]
        for j in range(end_x, start_x, -1):
            if j == start_x + 1:
                matrix[j][end_y] = temp1
            else:
                matrix[j][end_y] = matrix[j - 1][end_y]
            num = matrix[j][end_y]
            if min_num > num:
                min_num = num

        temp3 = matrix[end_x][start_y]
        for j in range(start_y, end_y):
            if j == end_y - 1:
                matrix[end_x][j] = temp2
            else:
                matrix[end_x][j] = matrix[end_x][j + 1]
            num = matrix[end_x][j]
            if min_num > num:
                min_num = num

        # temp4 = matrix[start_x][start_y]
        for j in range(start_x, end_x):
            if j == end_x - 1:
                matrix[j][start_y] = temp3
            else:
                matrix[j][start_y] = matrix[j + 1][start_y]
            num = matrix[j][start_y]
            if min_num > num:
                min_num = num

        answer.append(min_num)

    return answer


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(rows, columns, queries))
