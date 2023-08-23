import itertools


def solution(n, k):
    answer = []

    arr = [i for i in range(1, n + 1)]
    permutations = list(itertools.permutations(arr))
    answer = list(permutations[k - 1])

    return answer


def other_solution(n, k):
    answer = []

    result = []
    map = [False for _ in range(0, n + 1)]

    recursive(result, n, map, answer)

    result = answer[k - 1]

    return result


def recursive(result, n, map, arr):
    if len(result) == n:
        arr.append(result.copy())
        return

    for i in range(1, n + 1):
        if map[i] is False:
            map[i] = True
            result.append(i)
            recursive(result, n, map, arr)
            result.remove(i)
            map[i] = False


print(solution(3, 5))
