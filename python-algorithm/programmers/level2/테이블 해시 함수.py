def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    sum = 0
    for i in range(row_begin, row_end + 1):
        arr = sorted_data[i - 1]
        curr_sum = 0

        for num in arr:
            curr_sum += (num % i)

        sum ^= curr_sum

    answer = sum

    return answer


data = [[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]]
col = 2
row_begin = 2
row_end = 3
print(solution(data, col, row_begin, row_end))
