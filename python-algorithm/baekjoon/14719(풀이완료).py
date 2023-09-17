n, m = map(int, input().split())
height_list = list(map(int, input().split()))

max_height = 0
max_idx = 0
for i in range(m):
    if max_height < height_list[i]:
        max_height = height_list[i]
        max_idx = i

left = 0
right = m - 1

answer = 0

cur_height = height_list[0]
for i in range(left, max_idx):
    if cur_height < height_list[i]:
        cur_height = height_list[i]
    answer += (cur_height - height_list[i])

cur_height = height_list[m - 1]
for i in range(right, max_idx, -1):
    if cur_height < height_list[i]:
        cur_height = height_list[i]
    answer += (cur_height - height_list[i])

print(answer)
