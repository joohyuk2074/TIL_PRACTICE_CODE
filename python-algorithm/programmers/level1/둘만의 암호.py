def solution(s, skip, index):
    answer = ''

    for c in s:
        cnt = 0
        current_char = c
        next_char = ''
        while cnt < index:
            next_char = get_next_char(current_char)
            if next_char not in skip:
                cnt += 1
            current_char = next_char
        answer += next_char

    return answer


def get_next_char(c):
    if c == 'z':
        return 'a'
    else:
        return chr(ord(c) + 1)


s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))
