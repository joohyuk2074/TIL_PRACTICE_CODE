def solution(s):
    answer = 0

    count = len(s)
    for i in range(0, count):
        rotated_string = s[i:] + s[0:i]
        if validate(rotated_string):
            answer += 1

    return answer


def validate(rotated_string):
    stack = []

    for c in rotated_string:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        elif c == ']':
            if len(stack) == 0:
                return False

            if stack[-1] == '[':
                stack.pop()
        elif c == '}':
            if len(stack) == 0:
                return False

            if stack[-1] == '{':
                stack.pop()
        elif c == ')':
            if len(stack) == 0:
                return False

            if stack[-1] == '(':
                stack.pop()

    if len(stack) == 0:
        return True

    return False


s = "[](){}"
result = 3
print(solution(s))
