def solution(arr):
    arr_length = len(arr)
    if arr_length == 1:
        return arr

    q = 1
    while 2 ** q < arr_length:
        q += 1

    length = 2 ** q
    for i in range(0, length - arr_length):
        arr.append(0)

    return arr
