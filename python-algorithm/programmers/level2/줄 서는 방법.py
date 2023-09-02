def solution(n, k):
    answer = []

    num_arr = []
    for i in range(1, n + 1):
        num_arr.append(i)

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    arr = []
    while n:
        index = k // factorial(n - 1, dp)
        arr.append(num_arr[index])

        k %= factorial(n - 1, dp)

        n -= 1

    return answer


def factorial(number, dp):
    if dp[number - 1]:
        return dp[number - 1] * number

    result = 1
    for num in range(number, 1, -1):
        result *= num

    dp[number] = result
    return dp[number]


n = 3
k = 5
print(solution(n, k))
#
# dp = [0] * 1024
# arr = []
# print(factorial(4, dp))
