import itertools
import re


def solution(expression):
    answer = 0

    # 1. 피연산자와 연산자를 분리해서 각각의 배열에 삽입한다.
    operands = re.split(r'[-*+]', expression)
    operators = [op for op in re.split(r'\d', expression) if op]

    opt_arr = []
    index = 0
    while index < len(operators):
        opt_arr.append(operands[index])
        opt_arr.append(operators[index])
        index += 1
    opt_arr.append(operands[len(operands) - 1])

    permutations = itertools.permutations(['+', '*', '-'])
    for permutation in permutations:  # 각 우선순위별 연산자
        # print(opt_arr)
        # print(permutation)

        first_arr = []
        first_operator = permutation[0]
        generate(opt_arr, first_arr, first_operator)
        # print(first_arr)

        second_arr = []
        second_operator = permutation[1]
        generate(first_arr, second_arr, second_operator)
        # print(second_arr)

        third_arr = []
        third_operator = permutation[2]
        generate(second_arr, third_arr, third_operator)
        # print(third_arr)

        sum = abs(int(third_arr[0]))
        if answer < sum:
            answer = sum

        # print()

    return answer


def generate(prev_arr, current_arr, operator):
    index = 0

    while index < len(prev_arr):
        element = prev_arr[index]
        if element == operator:
            num1 = int(current_arr.pop())
            operator = element
            index += 1
            num2 = int(prev_arr[index])
            result = operation(num1, num2, operator)
            current_arr.append(str(result))
        else:
            current_arr.append(element)
        index += 1


def operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


expression = "100-200*300-500+20"
print(solution(expression))

expression1 = "50*6-3*2"
print(solution(expression1))
