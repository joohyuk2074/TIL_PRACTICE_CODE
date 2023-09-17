def is_longer_height_behind(cur_x, cur_height, x_to_y):
    for key in x_to_y:
        if cur_x < key:
            if cur_height < x_to_y[key]:
                return True
    return False


def get_one_depth_lower_height(cur_idx, cur_height, x_to_y):
    one_depth_height = 0

    for key in x_to_y:
        if cur_idx < key:
            if x_to_y[key] > one_depth_height:
                one_depth_height = x_to_y[key]

    if one_depth_height == 0:
        one_depth_height = cur_height

    return one_depth_height


n = int(input())
pillars = []
for _ in range(n):
    pillar = list(map(int, input().split()))
    pillars.append(pillar)

sorted_pillars = sorted(pillars, key=lambda x: x[0])

x_to_y = {}
for x, y in sorted_pillars:
    x_to_y[x] = y

start_x = sorted_pillars[0][0]
end_x = sorted_pillars[len(sorted_pillars) - 1][0]

is_up_flag = False
cur_height = x_to_y[start_x]

answer = cur_height
for i in range(start_x + 1, end_x + 1):
    if i in x_to_y:
        if is_longer_height_behind(i, x_to_y[i], x_to_y):
            if cur_height < x_to_y[i]:
                cur_height = x_to_y[i]
                answer += cur_height
        else:
            cur_height = x_to_y[i]
            if cur_height != get_one_depth_lower_height(i, cur_height, x_to_y):
                answer += cur_height
                cur_height = get_one_depth_lower_height(i, cur_height, x_to_y)
            else:
                answer += cur_height
    else:
        answer += cur_height

print(answer)
