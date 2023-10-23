n = int(input())
min_x, min_y = 10 ** 6, 10 ** 6
max_x, max_y = 0, 0

coordinates = []

for _ in range(n):
    x, y = map(int, input().split())

    if x < min_x:
        min_x = x

    if x > max_x:
        max_x = x

    if y < min_y:
        min_y = y

    if y > max_y:
        max_y = y

    coordinates.append((x, y))

map = [[0 for _ in range(max_x)] for _ in range(max_y)]

