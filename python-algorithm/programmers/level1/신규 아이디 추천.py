import re


def solution(new_id):
    answer = ''

    # 1단계 소문자로 변경
    converted_chars = []
    for char in new_id:
        if char.isalpha():
            converted_chars.append(char.lower())
        else:
            converted_chars.append(char)

    # 2단계 a-z, 0-9, -, _, . 를 제외한 모든 문자를 제거
    output_str = ''.join(converted_chars)
    converted_chars = []
    for char in output_str:
        if ord('a') <= ord(char) <= ord('z'):
            converted_chars.append(char)

        if ord('0') <= ord(char) <= ord('9'):
            converted_chars.append(char)

        if char == '-':
            converted_chars.append(char)

        if char == '_':
            converted_chars.append(char)

        if char == '.':
            converted_chars.append(char)

    # 3단계
    output_str = ''.join(converted_chars)
    output_str = re.sub(r'\.+', '.', output_str)

    # 4단계
    if len(output_str) == 1 and output_str[0] == '.':
        output_str = ''
    else:
        if output_str[0] == '.':
            output_str = output_str[1:]
        if output_str[-1] == '.':
            output_str = output_str[:-1]

    # 5단계
    if output_str == '':
        output_str = 'a'

    # 6단계
    if len(output_str) >= 16:
        output_str = output_str[:15]
        if output_str[-1] == '.':
            output_str = output_str[:-1]

        # 7단계
    if len(output_str) <= 2:
        current_char = output_str[-1]
        while len(output_str) <= 2:
            output_str += current_char

    answer = output_str

    return answer


print(solution("abcdefghijklmn.p"))
# print(solution("123_.def"))
# print(solution('...!@BaT#*..y.abcdefghijklm'))
# print(solution('.....'))
