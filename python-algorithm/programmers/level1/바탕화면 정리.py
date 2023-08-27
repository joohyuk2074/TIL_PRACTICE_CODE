def solution(wallpaper):
    answer = []
    #
    # for i in range(len(wallpaper)):
    #     print(wallpaper[i])
    #
    queue = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                queue.append((i, j))

    pair = queue.pop()
    left_north = [pair[0], pair[1]]
    right_north = [pair[0], pair[1]]
    while queue:
        x, y = queue.pop()
        if left_north[0] > x:
            left_north[0] = x

        if left_north[1] > y:
            left_north[1] = y

        if right_north[0] < x:
            right_north[0] = x

        if right_north[1] < y:
            right_north[1] = y

    answer.append(left_north[0])
    answer.append(left_north[1])
    answer.append(right_north[0] + 1)
    answer.append(right_north[1] + 1)

    return answer


wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper))

wallpaper1 = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
print(solution(wallpaper1))
