# https://school.programmers.co.kr/learn/courses/30/lessons/181938
def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = 2 * a * b
    return max(num1, num2)


print(solution(2, 91))
