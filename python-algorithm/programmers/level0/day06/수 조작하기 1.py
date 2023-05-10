def solution(n, control):
    for c in control:
        print(c)
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        elif c == "a":
            n -= 10

    return n


def other_solution(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


print(solution(0, "wsdawsdassw"))
