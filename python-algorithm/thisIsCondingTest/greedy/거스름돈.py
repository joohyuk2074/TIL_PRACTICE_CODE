def solution(n):
    answer = 0

    while n >= 500:
        n -= 500
        answer += 1

    while n >= 100:
        n -= 100
        answer += 1

    while n >= 50:
        n -= 50
        answer += 1

    while n >= 10:
        n -= 10
        answer += 1

    return answer


def other_solution(n):
    n = 1260
    count = 0

    list = [500, 100, 50, 10]
    for coin in list:
        count += n // coin
        n %= coin

    return count


print(solution(600))
