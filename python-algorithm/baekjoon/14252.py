def _gcd(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    return b


n = int(input())
input_list = sorted(list(map(int, input().split())))

count = 0
index = 0
while index < n - 1:
    first_number = input_list[index]
    second_number = input_list[index + 1]

    gcd = _gcd(first_number, second_number)
    if gcd > 1:
        for i in range(first_number, second_number):
            if _gcd(first_number, i) == 1 and _gcd(i, second_number) == 1:
                count += 1
                break

            if i == second_number - 1:
                count += 2

    index += 1

print(count)
