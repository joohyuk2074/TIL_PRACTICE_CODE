alpha_dict = {}
cnt = 0


def solution(word):
    answer = 0

    alpha = ['A', 'E', 'I', 'O', 'U']

    recursive('', alpha)

    answer = alpha_dict[word]

    return answer


def recursive(text, alpha):
    global cnt

    if text in alpha_dict:
        return

    if len(text) == 6:
        alpha_dict[text] = cnt
        return

    alpha_dict[text] = cnt
    cnt += 1

    for c in alpha:
        recursive(text + c, alpha)


print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))
print(solution('EIO'))
