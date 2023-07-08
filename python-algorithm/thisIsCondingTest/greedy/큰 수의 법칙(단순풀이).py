def solution(n, m, k, data):
    answer = 0

    data.sort()
    first_num = data[n - 1]
    second_num = data[n - 2]

    while m > 0:
        cnt = k
        while cnt > 0 and m > 0:
            answer += first_num
            m -= 1
            cnt -= 1

        if cnt <= 0 and m > 0:
            answer += second_num
            m -= 1
            cnt = k

    return answer


n, m, k = map(int, input().split())
data = list(map(int, input().split()))

print(solution(n, m, k, data))
