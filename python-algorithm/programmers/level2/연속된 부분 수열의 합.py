def solution(sequence, k):
    answer = []

    start_idx = 0
    end_idx = 0

    list = []

    current_num = sequence[start_idx]
    while start_idx < len(sequence):
        if current_num == k:
            list.append((start_idx, end_idx))
            current_num -= sequence[start_idx]
            start_idx += 1
        elif current_num > k:
            current_num -= sequence[start_idx]
            start_idx += 1
        elif current_num < k:
            end_idx += 1

            if end_idx >= len(sequence):
                break

            current_num += sequence[end_idx]

    min_length = 1_000_001
    min_start = 0
    min_end = 0
    for start, end in list:
        if min_length > end - start:
            min_length = end - start
            min_start = start
            min_end = end

    answer.append(min_start)
    answer.append(min_end)

    return answer




sequence1 = [1, 2, 3, 4, 5]
k1 = 7
print(solution(sequence1, k1))

sequence2 = [1, 1, 1, 2, 3, 4, 5]
k2 = 5
print(solution(sequence2, k2))

sequence3 = [2, 2, 2, 2, 2]
k3 = 6
print(solution(sequence3, k3))
