def solution(n):
    answer = []

    matrix = [[0] * n for _ in range(n)]
    sum = get_sum(n)

    count = 1
    x = -2
    y = -1
    limit = n + 1

    while count <= sum:
        # print(sum)
        # print(limit)
        # 위 -> 아래
        x += 2
        y += 1
        limit -= 1
        cnt = 0
        while cnt < limit:
            matrix[x][y] = count
            count += 1
            x += 1
            cnt += 1

        # 왼쪽 -> 오른쪽
        cnt = 0
        limit -= 1
        x -= 1
        y += 1
        while cnt < limit:
            matrix[x][y] = count
            count += 1
            y += 1
            cnt += 1

        # 대각선
        cnt = 0
        limit -= 1
        x -= 1
        y -= 2
        while cnt < limit:
            matrix[x][y] = count
            count += 1
            x -= 1
            y -= 1
            cnt += 1

    for i in range(n):
        for j in range(0, i + 1):
            answer.append(matrix[i][j])

    return answer


def get_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


print(solution(4))
