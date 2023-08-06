def solution(arr):
    answer = []

    num_dict = {0: 0, 1: 0}
    size = len(arr)
    dfs(arr, 0, 0, size, num_dict)

    answer.append(num_dict[0])
    answer.append(num_dict[1])

    return answer


def dfs(matrix, x, y, size, num_dict):
    if isSameNum(x, y, size, matrix):
        num_dict[matrix[x][y]] += 1
        return

    next_size = size // 2

    dfs(matrix, x, y, next_size, num_dict)
    dfs(matrix, x, y + next_size, next_size, num_dict)
    dfs(matrix, x + next_size, y, next_size, num_dict)
    dfs(matrix, x + next_size, y + next_size, next_size, num_dict)


def isSameNum(x, y, size, matrix):
    num = matrix[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != num:
                return False

    return True


arr = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]
print(solution(arr))
