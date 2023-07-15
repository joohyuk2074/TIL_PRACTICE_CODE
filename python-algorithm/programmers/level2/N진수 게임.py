def solution(n, t, m, p):
    answer = ''
    text = getStr(n, t * m + p)

    text = text[p - 1:]
    index = 0
    while t > 0:
        answer += text[index]
        index += m
        t -= 1

    return answer


def getStr(n, max):
    answer = '0'
    for i in range(1, max):
        result = ''
        s = i
        while s != 0:
            q = getQ(s % n)
            result = q + result
            s = s // n
        answer += result

    return answer


def getQ(num):
    if num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    else:
        return str(num)


print(solution(5, 2, 4, 2))
print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 2))
