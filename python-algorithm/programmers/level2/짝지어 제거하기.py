def solution(s):
    stack = ['A']

    for c in s:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 1:
        return 1
    else:
        return 0


i = solution("aaabbcccddddeeeeeeeeaabbccc")
print(i)
