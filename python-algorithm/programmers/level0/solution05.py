# https://school.programmers.co.kr/learn/courses/30/lessons/181936
import math


def my_solution(number, n, m):
    gcd = math.gcd(n, m)
    lcm = (n * m) // gcd
    if number % lcm == 0:
        return 1
    else:
        return -1


def other_solution(number, n, m):
    return int(bool(number % n == 0) & bool(number % m == 0))


print(other_solution(55, 10, 5))
