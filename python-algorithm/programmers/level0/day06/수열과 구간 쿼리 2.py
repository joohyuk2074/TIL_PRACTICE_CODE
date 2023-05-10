def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        sub_array = arr[s:e + 1]
        sub_array.sort()

        flag = False
        for num in sub_array:
            if num > k:
                answer.append(num)
                flag = True
                break
        if flag is False:
            answer.append(-1)

    return answer


arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]
print(solution(arr, queries))
