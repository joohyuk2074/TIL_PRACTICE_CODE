def solution(before, after):
    before_list = [0] * 26
    for c in before:
        before_list[ord(c) - ord('a')] += 1

    after_list = [0] * 26
    for a in after:
        after_list[ord(a) - ord('a')] += 1

    for i in range(0, 26):
        if before_list[i] != after_list[i]:
            return 0

    return 1


def other_solution1(before, after):
    before = sorted(before)
    after = sorted(after)
    if before == after:
        return 1
    else:
        return 0


def other_solution1(before, after):
    return 1 if sorted(before) == sorted(after) else 0


print(solution("olleh", "hello"))
