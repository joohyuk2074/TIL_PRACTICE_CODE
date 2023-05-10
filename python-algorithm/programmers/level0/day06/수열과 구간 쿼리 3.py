def solution(arr, queries):
    answer = []

    for i in range(len(queries)):
        idx1 = queries[i][0]
        idx2 = queries[i][1]

        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    return arr
        
