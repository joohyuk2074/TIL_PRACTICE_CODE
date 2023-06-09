import sys

sys.setrecursionlimit(10 ** 7)

length_list = [0] * 2001


def solution(n):
    answer = 0

    answer = recursive(0, n)

    return answer % 1234567


def recursive(length, n):
    if length > n:
        return 0

    if length == n:
        return 1

    if length_list[length] > 0:
        return length_list[length]

    length_list[length + 1] = recursive(length + 1, n) % 1234567
    length_list[length + 2] = recursive(length + 2, n) % 1234567

    return length_list[length + 1] + length_list[length + 2]


def other_solution(num):
    a, b = 1, 2
    for i in range(2, num):
        a, b = b, a + b
    return b


print(other_solution(4))
