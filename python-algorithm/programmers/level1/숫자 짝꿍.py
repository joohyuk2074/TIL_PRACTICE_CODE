def solution(X, Y):
    answer = ''

    x_dict = {}
    y_dict = {}
    common_text = ''

    for c in X:
        if c not in x_dict:
            x_dict[c] = 1
        else:
            x_dict[c] += 1

    for c in Y:
        if c not in y_dict:
            y_dict[c] = 1
        else:
            y_dict[c] += 1

    for i in range(0, 9):
        x_cnt = 0
        if str(i) in x_dict:
            x_cnt = x_dict[str(i)]

        y_cnt = 0
        if str(i) in y_dict:
            y_cnt = y_dict[str(i)]

        if x_cnt <= y_cnt:
            common_text = common_text + (str(i) * x_cnt)
        else:
            common_text = common_text + (str(i) * y_cnt)

    if len(common_text) == 0:
        return '-1'

    result = common_text[::-1]

    if result[0] == '0':
        return '0'

    answer = result

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
