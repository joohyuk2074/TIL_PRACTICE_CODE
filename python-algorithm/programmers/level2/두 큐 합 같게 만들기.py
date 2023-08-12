def solution(queue1, queue2):
    answer = -1

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    pivot = (queue1_sum + queue2_sum) // 2

    queue1_idx = 0
    queue2_idx = 0
    t = len(queue1)

    while queue1_idx < 2 * t and queue2_idx < 2 * t and queue1_sum != queue2_sum:
        if queue1_sum < pivot:
            queue1_sum += queue2[queue2_idx]
            queue2_sum -= queue2[queue2_idx]
            queue1.append(queue2[queue2_idx])
            queue2_idx += 1
        else:
            queue1_sum -= queue1[queue1_idx]
            queue2_sum += queue1[queue1_idx]
            queue2.append(queue1[queue1_idx])
            queue1_idx += 1

    if queue1_sum == pivot:
        answer = queue1_idx + queue2_idx

    return answer


#
# queue1 = [3, 2, 7, 2]
# queue2 = [4, 6, 5, 1]
# print(solution(queue1, queue2))

queue1_1 = [1, 2, 1, 2]
queue2_2 = [1, 10, 1, 2]
print(solution(queue1_1, queue2_2))
