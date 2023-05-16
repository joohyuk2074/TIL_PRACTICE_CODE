def solution(array, n):
    arr = [0] * 1001
    for num in array:
        arr[num] += 1

    return arr[n]


def other_solution(array, n):
    return array.count(n)
