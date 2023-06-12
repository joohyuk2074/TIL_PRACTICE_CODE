def solution(elements):
    length = len(elements)

    arr = [[0 for _ in range(length)] for _ in range(length)]

    num_set = set()
    for i in range(0, length):
        arr[i][i] = elements[i]

    for i in range(0, length):
        for l in range(i + 1, length):
            arr[i][l] = arr[i][l - 1] + elements[l]

    for i in range(0, length):
        for l in range(i + 1, length):
            arr[l][i] = arr[l][length - 1] + arr[0][i]

    for i in range(0, length):
        for j in range(0, length):
            num_set.add(arr[i][j])

    return len(num_set)


def other_solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i + 1, i + ll):
            ssum += elements[j % ll]
            res.add(ssum)
    return len(res)


elements = [7, 9, 1, 1, 4]
print(solution(elements))
