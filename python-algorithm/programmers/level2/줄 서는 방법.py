memo = {}


def solution(n, k):
    answer = []

    num_arr = []
    for i in range(1, n + 1):
        num_arr.append(i)

    memo[0] = 1
    memo[1] = 1
    factorial(n)

    arr = []
    k -= 1
    while n:
        n -= 1
        index = k // memo[n]
        arr.append(num_arr[index])
        k %= memo[n]
        num_arr.pop(index)

    answer = arr

    return answer


def factorial(n):
    if n in memo:
        return memo[n]

    memo[n] = n * factorial(n - 1)
    return memo[n]


n = 3
k = 5
print(solution(n, k))
#
# dp = [0] * 1024
# arr = []
# print(factorial(4, dp))
