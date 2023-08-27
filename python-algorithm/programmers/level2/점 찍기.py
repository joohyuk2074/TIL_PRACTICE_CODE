import math


def solution(k, d):
    answer = 0

    y = 0
    for num in range(0, d + 1, k):  # 좌표를 k 배수만큼 증가
        y_possible_distance = int(math.sqrt(d ** 2 - num ** 2))
        cnt = y_possible_distance // k + 1
        answer += cnt

    return answer


k1 = 2
d1 = 4
print(solution(k1, d1))

k2 = 1
d2 = 5
print(solution(k2, d2))
