def solution(n, left, right):
    answer = []

    start_row = left // n
    end_row = right // n

    for i in range(start_row, end_row + 1):
        if i == start_row:
            start_col = left % n
        else:
            start_col = 0

        if i == end_row:
            end_col = right % n
        else:
            end_col = n - 1

        for j in range(start_col, end_col + 1):
            index = max(i, j)
            answer.append(index + 1)

    return answer


def other_solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    return answer


print(solution(4, 7, 14))
