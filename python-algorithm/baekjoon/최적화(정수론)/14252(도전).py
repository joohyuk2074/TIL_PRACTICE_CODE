def gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b


n = int(input())
numbers = sorted(list(map(int, input().split())))

count = 0
index = 0
while index < n - 1:
    start_num = numbers[index]
    end_num = numbers[index - 1]

    if gcd(start_num, end_num) > 1:
        for mid_num in range(start_num + 1, end_num):
            if gcd(start_num, mid_num) == 1 and gcd(mid_num, end_num) == 1:
                count += 1
                break

            if mid_num == end_num - 1:
                count += 2
                break

    index += 1

print(count)
