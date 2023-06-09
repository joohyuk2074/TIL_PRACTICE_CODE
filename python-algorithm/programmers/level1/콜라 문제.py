def solution(a, b, n):
    answer = 0

    while n >= a:
        p = n // a
        n = n - (p * a) + (p * b)
        answer += (p * b)

    return answer


other_solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

print(other_solution(2, 1, 20))
print(other_solution(3, 1, 20))
