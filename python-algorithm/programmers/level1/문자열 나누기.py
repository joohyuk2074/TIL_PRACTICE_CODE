def solution(s):
    answer = 0

    alpha_to_num_dict = {}
    is_first = True
    pivot_alpha = ''
    for i in range(len(s)):
        if is_first:
            pivot_alpha = s[i]
            alpha_to_num_dict[pivot_alpha] = 0
            alpha_to_num_dict['X'] = 0
            is_first = False

        if pivot_alpha == s[i]:
            alpha_to_num_dict[pivot_alpha] += 1
        else:
            alpha_to_num_dict['X'] += 1

        if alpha_to_num_dict[pivot_alpha] == alpha_to_num_dict['X']:
            answer += 1
            alpha_to_num_dict.clear()
            is_first = True

    if alpha_to_num_dict and (alpha_to_num_dict[pivot_alpha] != 0 or alpha_to_num_dict['X'] != 0):
        answer += 1

    return answer


def other_solution(s):
    answer = 0
    sav1 = 0
    sav2 = 0
    for i in s:
        if sav1 == sav2:
            answer += 1
            a = i
        if i == a:
            sav1 += 1
        else:
            sav2 += 1


str1 = "banana"
str2 = "abracadabra"
str3 = "aaabbaccccabba"
print(solution(str1))
print(solution(str2))
print(solution(str3))
