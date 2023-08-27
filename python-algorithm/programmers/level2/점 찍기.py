import math


def solution(k, d):
    answer = 0

    n = d // k
    for a in range(0, n + 1):
        for b in range(0, n + 1):
            if possible(a * k, b * k, d):
                answer += 1

    return answer


def possible(x, y, d):
    return math.sqrt(x ** 2 + y ** 2) <= d


k1 = 2
d1 = 4
print(solution(k1, d1))

k2 = 1
d2 = 5
print(solution(k2, d2))
