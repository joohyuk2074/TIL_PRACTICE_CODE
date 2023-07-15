import math

def solution(number, limit, power):
    answer = 0

    for knights_num in range(1, number + 1):
        divisor_num = getDivisorNum(knights_num)
        if divisor_num > limit:
            answer += power
        else:
            answer += divisor_num

    return answer


def getDivisorNum(num):
    count = 0

    sqrt_num_floor = int(math.sqrt(num))
    for i in range(1, sqrt_num_floor + 1):
        if num % i == 0:
            count += 2
        if num / i == i:
            count -= 1

    return count


print(solution(5, 3, 2))
