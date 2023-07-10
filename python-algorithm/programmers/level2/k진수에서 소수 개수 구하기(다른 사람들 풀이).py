import math


def solution(n, k):
    answer = 0

    # sieve_of_eratosthenes(n)
    # global primes
    # primes = [False for _ in range(0, n + 1)]

    number = getNumber(k, n)
    numbers = number.split('0')

    for str_num in numbers:
        if len(str_num) != 0:
            num = int(str_num)
            if num > 1 and isMinority(num):
                answer += 1
            # if isMinority(num):
            #     answer += 1

    return answer


def getNumber(k, n):
    num = ""
    while n >= k:
        p = n // k
        q = n % k
        num = str(q) + num
        n = p
    num = str(n) + num
    return num


def isMinority(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


#
#
# def sieve_of_eratosthenes(n):
#     # 불리언 값으로 채워진 배열을 만듭니다. 처음에는 모든 숫자가 소수라고 가정합니다.
#     global primes
#     primes = [True for i in range(n + 1)]
#
#     p = 2
#     while p * p <= n:
#         # p가 아직 지워지지 않았다면, 그것은 소수입니다.
#         if primes[p]:
#             # p의 모든 배수를 지웁니다.
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1


print(solution(110011, 10))
