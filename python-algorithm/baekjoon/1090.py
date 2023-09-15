# 체커
answer = [0]

n = int(input())
coordinate_list = [list(map(int, input().split())) for _ in range(4)]
sorted_coordinate_list = sorted(coordinate_list, key=lambda p: p[0] ** 2 + p[1] ** 2)

for member_cnt in range(2, n + 1):

    min_length = 1_000_000 * 1_000_000

    start_idx = 0
    while start_idx + member_cnt <= n:

        mid_x = 0
        mid_y = 0
        for i in range(start_idx, start_idx + member_cnt):
            mid_x += coordinate_list[i][0]
            mid_y += coordinate_list[i][1]
        mid_x //= member_cnt
        mid_y //= member_cnt

        sum = 0
        for i in range(start_idx, start_idx + member_cnt):
            coordinate = coordinate_list[i]
            sum += abs(mid_x - coordinate[0]) + abs(mid_y - coordinate[1])

        if min_length > sum:
            min_length = sum

        start_idx += 1

    answer.append(min_length)

print(answer)

# 모든 위치에서
# 모든 친구들의 거리를 계산해서
# 가장 적은 값을 알려주면 되겠죠 !

# 1번 아이디어
# X, Y를 구분해서 계산해준 뒤에 합쳐서
# 최솟값을 알려주면 됩니다!

# 2번 아이디어
# X, Y를 구분해서 계산해준 뒤에 합쳐서
# 최솟값을 알려주면 됩니다!

# 3번 아이디어
# 최소 거리를 계산하고 싶다.
# 그리고, 2명이 모여야한다.
# 그 점에서, 가까운 두명의 거리만 더해주면 되지 않을까

# A번집 B번집 C번집

# [1, 2, 3] / [3, 4, 5,] / [2, 2, 5]

# 두 사람이 모일 수 있는 최소거리는 -> 3!
