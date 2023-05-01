# https://school.programmers.co.kr/learn/courses/30/lessons/181937
def solution(num, n):
    return int(bool(num % n == 0))


print(solution(34, 3))