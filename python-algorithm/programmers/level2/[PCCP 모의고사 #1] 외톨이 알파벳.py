def solution(input_string):
    answer = ''

    dict = {}
    prev_c = ''
    for c in input_string:
        if prev_c != c:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
            prev_c = c

    for key in dict:
        if dict[key] >= 2:
            answer += key

    if len(answer) == 0:
        return "N"

    answer = ''.join(sorted(answer))
    return answer


input_strping = "edeaaabbccd"
print(solution(input_strping))
