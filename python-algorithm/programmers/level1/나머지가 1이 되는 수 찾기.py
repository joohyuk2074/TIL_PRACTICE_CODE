def solution(n):
    answer = 0

    multi = 1
    for num in range(2, n):
        # 2 ~ n
        while num * multi + 1 <= n:
            if num * multi + 1 == n:
                return num
            else:
                multi += 1
        multi = 1

    return answer


def other_solution(n):
    return [x for x in range(1, n+1) if n % x == 1][0]
