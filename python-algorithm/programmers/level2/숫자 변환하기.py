def solution(x, y, n):
    answer = 0

    d = [-1] * 1_000_001
    d[x] = 0

    for i in range(x, y + 1):
        if d[i] != -1:
            if i + n <= y:
                if d[i + n] == -1:
                    d[i + n] = d[i] + 1
                elif d[i + n] != -1:
                    d[i + n] = min(d[i] + 1, d[i + n])
            if i * 2 <= y:
                if d[i * 2] == -1:
                    d[i * 2] = d[i] + 1
                elif d[i * 2] != -1:
                    d[i * 2] = min(d[i] + 1, d[i * 2])
            if i * 3 <= y:
                if d[i * 3] == -1:
                    d[i * 3] = d[i] + 1
                elif d[i * 3] != -1:
                    d[i * 3] = min(d[i] + 1, d[i * 3])

    return d[y]


x = 10
y = 40
n = 5
print(solution(x, y, n))
x1 = 10
y1 = 40
n1 = 30
print(solution(x1, y1, n1))
x2 = 2
y2 = 5
n2 = 4
print(solution(x2, y2, n2))
