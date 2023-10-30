n = int(input())

x_to_height_dict = {}
infos = []
max_height = 0
for _ in range(n):
    x, height = map(int, input().split())
    if max_height < height:
        max_height = height
    infos.append([x, height])
    x_to_height_dict[x] = height

sorted_data = sorted(infos, key=lambda x: x[0])

start_x = sorted_data[0][0]
end_x = sorted_data[n - 1][0]

max_height_x_list = []
for x, height in infos:
    if height == max_height:
        max_height_x_list.append(x)

max_start_x = max_height_x_list[0]
max_end_x = max_height_x_list[len(max_height_x_list) - 1]

# start ~ max_start_x 까지 면적구하기
current_height = 0
left_sum = 0
for i in range(start_x, max_start_x):
    if i in x_to_height_dict:
        if x_to_height_dict[i] > current_height:
            current_height = x_to_height_dict[i]
    left_sum += current_height

# max_start_x ~ max_end_x 까지의 면적구하기
mid_sum = (max_end_x - max_start_x + 1) * max_height

# max_end_x ~ end_x 까지 면적 구하기
current_height = 0
right_sum = 0
for i in range(end_x, max_end_x, -1):
    if i in x_to_height_dict:
        if x_to_height_dict[i] > current_height:
            current_height = x_to_height_dict[i]
    right_sum += current_height

print(left_sum + mid_sum + right_sum)
