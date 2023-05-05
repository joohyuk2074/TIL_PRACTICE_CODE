def solution(num_list):
    multiple_sum = 1
    for i in range(len(num_list)):
        multiple_sum *= num_list[i]

    square_sum = 0
    for i in range(len(num_list)):
        square_sum += num_list[i]
    square_sum = square_sum ** 2

    print(multiple_sum)
    print(square_sum)

    if multiple_sum < square_sum:
        return 1
    elif multiple_sum > square_sum:
        return 0


def other_solution(num_list):
    s = sum(num_list) ** 2
    m = eval('*'.join([str(n) for n in num_list]))
    return 1 if s > m else 0


print(solution([3, 4, 5, 2, 1]))
