def solution(str1, str2):
    answer = ''

    arr1 = list(str1)
    arr2 = list(str2)
    for i in range(min(len(arr1), len(arr2))):
        answer += arr1[i] + arr2[i]

