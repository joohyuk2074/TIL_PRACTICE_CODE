def solution(dot):
    x = dot[0]
    y = dot[1]

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def other_solution(dot):
    quad = [(3, 2), (4, 1)]
    return quad[dot[0] > 0][dot[1] > 0]
