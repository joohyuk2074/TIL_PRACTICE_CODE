def solution(s):
    answer = []

    binary_cnt = 0
    deleted_zero_num = 0
    while s != '1':
        deleted_zero_num += s.count('0')
        binary_cnt += 1

        s_without_zeros = s.replace('0', '')
        length = len(s_without_zeros)
        s = str(bin(length)[2:])

    answer.append(binary_cnt)
    answer.append(deleted_zero_num)

    return answer


def other_solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]

    return [a, b]


s = "110010101001"
l = solution(s)
print(l)
