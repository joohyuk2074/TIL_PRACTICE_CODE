def solution(n, m, section):
    answer = 0

    start = section[0]
    end = section[0] + m - 1
    answer += 1

    for s in section:
        if start <= s <= end:
            continue
        else:
            start = s
            end = s + m - 1
            answer += 1

    return answer


n = 8
m = 4
section = [2, 3, 6]
print(solution(n, m, section))
