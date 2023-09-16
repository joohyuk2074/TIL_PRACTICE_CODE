# 청기 백기
# 청기 백기 0, 백기 청기 1

def count_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


n = int(input())
answer = 0
for number in range(1, n + 1):
    count = len(count_divisors(number))
    if count % 2 != 0:
        answer += 1

print(answer)

# number의 약수를 모두 구한다
