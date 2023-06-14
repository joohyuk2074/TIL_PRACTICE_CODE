def solution(order):
    answer = 0

    stack = []
    index = 0
    for i in range(1, len(order) + 1):
        if order[index] == i:
            answer += 1
            index += 1
        else:
            stack.append(i)

        while stack and index < len(order):
            if stack[-1] == order[index]:
                stack.pop()
                answer += 1
                index += 1
            else:
                break

    return answer


order1 = [4, 3, 1, 2, 5]
order2 = [5, 4, 3, 2, 1]
print(solution(order1))
print(solution(order2))
