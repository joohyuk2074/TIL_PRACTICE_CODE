from collections import Counter


def solution(X, Y):
    answer = ''
    X = Counter(X)
    Y = Counter(Y)

    for i in range(9, -1, -1):
        mn = min(X[str(i)], Y[str(i)])
        answer += str(i) * mn

    if answer == "":
        return "-1"

    if answer[0] == "0":
        return "0"

    return answer


X1 = "100"
Y1 = "2345"
print(solution(X1, Y1))

X2 = "100"
Y2 = "203045"
print(solution(X2, Y2))

X3 = "100"
Y3 = "123450"
print(solution(X3, Y3))

X4 = "12321"
Y4 = "42531"
print(solution(X4, Y4))

X5 = "5525"
Y5 = "1255"
print(solution(X5, Y5))

X6 = "1000000002"
Y6 = "20200"
print(solution(X6, Y6))
