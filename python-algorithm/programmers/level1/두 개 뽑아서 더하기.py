def solution(numbers):
    answer = []

    num_set = set()
    recursive(0, 0, 0, num_set, numbers)

    answer = list(num_set)

    return sorted(answer)


def recursive(index, total, count, num_set, numbers):
    if count == 2:
        num_set.add(total)
        return

    if index >= len(numbers):
        return

    recursive(index + 1, total + numbers[index], count + 1, num_set, numbers)
    recursive(index + 1, total, count, num_set, numbers)


def other_solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(answer))
