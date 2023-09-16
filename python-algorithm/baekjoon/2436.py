gcd, lcm = map(int, input().split())
maxg = gcd * lcm


def _gcd(a, b):
    while a % b != 0:
        mod = a % b
        a = b
        b = mod
    return b


def _lcm(a, b):
    return a * b // _gcd(a, b)


answer = []

for i in range(gcd, int(maxg ** 0.5) + 1, gcd):
    if _gcd(i, (maxg // i)) == gcd and _lcm(i, (maxg // i)) == lcm:
        answer.append((i, maxg // i))

print(*answer[-1])
