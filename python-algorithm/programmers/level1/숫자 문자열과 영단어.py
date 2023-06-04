map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solution(s):
    answer = 0

    if s.isdigit():
        return int(s)

    result = ''
    key = ''
    for c in s:
        if c.isdigit():
            result += c
        else:
            key += c
            if key in map:
                result += map.get(key)
                key = ''

    return int(result)


def other_solution(s):
    answer = s
    for key, value in map.items():
        answer = answer.replace(key, value)
    return int(answer)


text = "23four5six7"
print(solution(text))
