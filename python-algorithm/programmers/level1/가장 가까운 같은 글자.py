def solution(s):
    answer = []

    arr = {}
    for i in range(ord('a'), ord('z') + 1):
        arr[chr(i)] = -1

    for i in range(0, len(s)):
        if arr[s[i]] == -1:
            answer.append(-1)
        else:
            num = i - arr[s[i]]
            answer.append(num)
        arr[s[i]] = i

    return answer


def other_solution(s):
    answer = []
    dic = dict()

    for i in range(len(s)):
        if s[i] not in dict:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer


print(solution("banana"))
