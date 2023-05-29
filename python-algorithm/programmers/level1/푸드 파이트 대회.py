def solution(food):
    answer = ''

    for i in range(0, len(food)):
        n = food[i] // 2
        for _ in range(0, n):
            answer += str(i)

    reversed_answer = answer[::-1]

    answer = answer + '0' + reversed_answer

    return answer


def other_solution(food):
    answer = "0"
    for i in range(len(food) - 1, 0, -1):
        c = int(food[i] / 2)
        while c > 0:
            answer = str(i) + answer + str(i)
            c -= 1


food = [1, 3, 4, 6]
print(solution(food))
