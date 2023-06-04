def solution(sizes):
    answer = 0

    widths = []
    heights = []

    for width, height in sizes:
        if width < height:
            widths.append(height)
            heights.append(width)
        else:
            widths.append(width)
            heights.append(height)

    w_max = max(widths)
    h_max = max(heights)

    return w_max * h_max


def other_solution(sizes):
    return max(max(x) for x in sizes * max(min(x) for x in sizes))
