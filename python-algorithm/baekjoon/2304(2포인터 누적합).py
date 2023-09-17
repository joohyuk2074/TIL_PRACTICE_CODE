n = int(input())
pillars = []
for _ in range(n):
    pillar = list(map(int, input().split()))
    pillars.append(pillar)

sorted_pillars = sorted(pillars, key=lambda x: x[0])

max_height = 0
max_idx = 0
for pillar in sorted_pillars:
    if max_height < pillar[1]:
        max_height = pillar[1]
        max_idx = pillar[0]

x_to_y = {}
for x, y in sorted_pillars:
    x_to_y[x] = y

left = sorted_pillars[0][0]
right = sorted_pillars[len(sorted_pillars) - 1][0]

answer = max_height

cur_height = sorted_pillars[0][1]
for i in range(left, max_idx):
    if i in x_to_y:
        if cur_height < x_to_y[i]:
            cur_height = x_to_y[i]
    answer += cur_height

cur_height = sorted_pillars[len(sorted_pillars) - 1][1]
for i in range(right, max_idx, -1):
    if i in x_to_y:
        if cur_height < x_to_y[i]:
            cur_height = x_to_y[i]
    answer += cur_height

print(answer)
