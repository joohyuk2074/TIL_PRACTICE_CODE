def solution(park, routes):
    answer = []

    button = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    row_length = len(park)
    column_length = len(park[0])

    x, y = 0, 0
    for i in range(row_length):
        for j in range(column_length):
            if park[i][j] == 'S':
                x = i
                y = j

    for route in routes:
        split = route.split(" ")
        direction = split[0]
        edge = int(split[1])

        pair = button[direction]
        dx = pair[0]
        dy = pair[1]

        stack = []
        while edge:
            x += dx
            y += dy
            stack.append((-1 * dx, -1 * dy))
            if 0 <= x < row_length and 0 <= y < column_length and park[x][y] != 'X':
                edge -= 1
                continue
            else:
                while stack:
                    pop = stack.pop()
                    x += pop[0]
                    y += pop[1]
                break

    answer = [x, y]

    return answer


park = ["SOO", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]
print(solution(park, routes))

park1 = ["OSO", "OOO", "OXO", "OOO"]
routes1 = ["E 2", "S 3", "W 1"]
print(solution(park1, routes1))
