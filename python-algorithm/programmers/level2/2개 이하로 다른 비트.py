def solution_timeout(numbers):
    answer = []

    for current_number in numbers:
        bin_current_number = change_bin_str(current_number)

        next_number = current_number + 1
        while True:
            bin_next_number = change_bin_str(next_number)

            current_number_stack = []
            next_number_stack = []
            for c in bin_current_number:
                current_number_stack.append(c)

            for c in bin_next_number:
                next_number_stack.append(c)

            cnt = 0
            while len(current_number_stack) != 0 and len(next_number_stack) != 0:
                c_number = current_number_stack.pop()
                n_number = next_number_stack.pop()
                if c_number != n_number:
                    cnt += 1

            cnt += len(next_number_stack)

            if cnt <= 2:
                break

            next_number += 1

        answer.append(next_number)

    return answer


def change_bin_str(number):
    return bin(number).replace('0b', '')
#
#
# def solution(numbers):
#     answer = []



numbers = [2, 7]
print(solution(numbers))
