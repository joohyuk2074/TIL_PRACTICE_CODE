from collections import deque


def solution(dartResult):
    answer = 0

    deq = deque()

    index = 0
    while index < len(dartResult):
        if dartResult[index].isdigit():
            number = 0
            if dartResult[index + 1].isdigit():
                number = int(dartResult[index] + dartResult[index + 1])
                index += 1
            else:
                number = int(dartResult[index])

            if dartResult[index + 1] == 'S':
                number **= 1
            elif dartResult[index + 1] == 'D':
                number **= 2
            elif dartResult[index + 1] == 'T':
                number **= 3
            deq.append(number)
            index += 1
        elif dartResult[index] == '#':
            deq.append(deq.pop() * (-1))
        elif dartResult[index] == '*':
            num1 = deq.pop()

            num2 = 0
            if deq:
                num2 = deq.pop()
            if num2 != 0:
                deq.append(num2 * 2)
            deq.append(num1 * 2)

        index += 1

    while deq:
        answer += deq.popleft()

    return answer


result = solution("1D2S3T*")
print(result)
