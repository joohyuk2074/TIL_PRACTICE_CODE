def _gcd(a, b):
    while a % b != 0:  # 나머지가 0이 되는 순간 멈춘다.
        tmp = a % b
        a = b
        b = tmp
    return b


def _lcm(a, b):
    return a * b // _gcd(a, b)


a, b = map(int, input().split())

answer = []
pivot_number = 200000000
for number1 in range(2, int(100000001 ** 0.5) + 1):
    total_multiple_number = a * b
    if total_multiple_number % number1 == 0:
        number2 = total_multiple_number // number1
        print(number1, number2)
        if number1 + number2 < pivot_number:
            pivot_number = number1 + number2
            answer = [number1, number2]

print(sorted(answer))
