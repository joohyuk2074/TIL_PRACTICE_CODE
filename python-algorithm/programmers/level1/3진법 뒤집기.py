def solution(n):
    answer = 0

    s = ""
    while n > 0:
        m = n % 3  # 나머지
        n = n // 3  # 몫
        s += str(m)

    for c in s:
        answer = answer * 3 + int(c)

    return answer


def other_solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3) # 3진법인 tmp를 10진수로 변환
    return answer


print(solution(45))
