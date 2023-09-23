# 퇴사
def recursive(idx, total_price):
    global max_price

    if idx == n:
        max_price = max(max_price, total_price)
        return

    if (idx + counselling_schedules[idx][0]) <= n:
        recursive(idx + counselling_schedules[idx][0], total_price + counselling_schedules[idx][1])

    recursive(idx + 1, total_price)


n = int(input())
counselling_schedules = []
for _ in range(n):
    counselling_schedules.append(list(map(int, input().split())))

max_price = -1

recursive(0, 0)

print(max_price)
