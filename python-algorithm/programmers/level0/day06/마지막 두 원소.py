def solution(num_list):
    length = len(num_list)
    num1 = num_list[length - 2]
    num2 = num_list[length - 1]

    result = 0
    if num1 < num2:
        result = num2 - num1
    else:
        result = num2 * 2

    num_list.append(result)

    return num_list


def other_solution(num_list):
    num_list.append(num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1] * 2)
