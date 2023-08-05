from itertools import permutations


def solution(numbers):
    answer = 0

    # 소수 구하기
    limit = 9_999_999
    prime = [False, False] + [True] * (limit - 1)
    primes = []

    for i in range(2, int(limit ** 0.5) + 1):
        if prime[i]:
            primes.append(i)
            for j in range(i * 2, limit + 1, i):
                prime[j] = False

    for i in range(int(limit ** 0.5) + 1, limit + 1):
        if prime[i]:
            primes.append(i)

    # 숫자의 모든 경우의 수 구하기
    # 각 자리수에 대한 순열을 생성합니다.
    number_set = set()
    for i in range(len(numbers) + 1):  # 1자리, 2자리, 3자리 숫자를 생성
        for p in permutations(numbers, i):
            number = "".join(p)
            if len(number) > 0:
                number_set.add(int(number))

    for num in number_set:
        if prime[num]:
            answer += 1

    return answer


print(solution("011"))
print(solution("17"))
