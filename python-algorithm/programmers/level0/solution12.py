# https://school.programmers.co.kr/learn/courses/30/lessons/181935

def solution(n):
    answer = 0

    if n % 2 == 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i)
                answer += (i * i)
    else:
        for i in range(1, n + 1):
            if i % 2 == 1:
                print(i)
                answer += i

    return answer


def other_solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)


print(solution(10))
