def solution(arr, target):
    answer = False
    arr.sort()

    l = 0
    r = len(arr) - 1

    while l < r:
        if arr[l] + arr[r] == target:
            answer = True
            break
        elif arr[l] + arr[r] < target:
            l += 1
        else:
            r -= 1

    return answer


input = [4, 1, 9, 7, 5, 3, 16]
print(solution(input, 14))
