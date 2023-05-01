# https://school.programmers.co.kr/learn/courses/30/lessons/181939

def solution(a, b):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))

    if num1 >= num2:
        return num1
    else:
        return num2


def other_solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


print(solution(9, 91))