def solution(l, r):
    answer = []

    recursive(l, r, '5', answer)

    if len(answer) == 0:
        return [-1]

    answer.sort()
    return answer


def recursive(start, end, num, arr):
    if start > int(num) or int(num) > end:
        return

    arr.append(int(num))

    recursive(start, end, num + '5', arr)
    recursive(start, end, num + '0', arr)


def other_solution(l, r):
    answer = []

    queue = ['5']
    while queue:
        num = queue.pop(0)
        if l <= int(num) <= r:
            answer.append(int(num))
        if int(num) < r:
            queue.append(num + '0')
            queue.append(num + '5')

    if len(answer) == 0:
        return [-1]

    return answer


print(other_solution(5, 555))
