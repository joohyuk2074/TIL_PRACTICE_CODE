def solution(arrayA, arrayB):
    answer = 0

    minA = min(arrayA)
    minB = min(arrayB)

    count = 0
    if minA < minB:
        count = minB
    else:
        count = minA

    results = []
    for num in range(2, count + 1):
        a_set = set()
        b_set = set()

        for a in arrayA:
            if a % num == 0:
                a_set.add(a)

        for b in arrayB:
            if b % num == 0:
                b_set.add(b)

        if len(a_set) == len(arrayA) and len(b_set) == 0:
            results.append(num)
        elif len(b_set) == len(arrayB) and len(a_set) == 0:
            results.append(num)

    if len(results) == 0:
        return 0

    answer = max(results)

    return answer


def other_solution(arrayA, arrayB):
    # 각 배열의 최대공약수를 찾는다
    first_num_a = arrayA[0]
    for i in range(1, len(arrayA)):
        first_num_a = gcd(first_num_a, arrayA[i])

    first_num_b = arrayB[0]
    for i in range(1, len(arrayB)):
        first_num_b = gcd(first_num_b, arrayB[i])

    # 각 최대공약수로 반대 배열의 숫자를 나눌 수 있는지 확인한다.
    a_flag = True
    for a in arrayA:
        if a % first_num_b == 0:
            a_flag = False
            break

    b_flag = True
    for b in arrayB:
        if b % first_num_a == 0:
            b_flag = False
            break

    if a_flag is False and b_flag is False:
        return 0

    if a_flag and b_flag:
        if first_num_a < first_num_b:
            return first_num_b
        else:
            return first_num_a
    elif b_flag:
        return first_num_a
    elif a_flag:
        return first_num_b


def gcd(a, b):
    while b:
        remainder = a % b
        a = b
        b = remainder

    return a


arrayA2 = [10, 17]
arrayB2 = [5, 20]
print(other_solution(arrayA2, arrayB2))

arrayA1 = [10, 20]
arrayB1 = [5, 17]
print(other_solution(arrayA1, arrayB1))

arrayA = [14, 35, 119]
arrayB = [18, 30, 102]
print(other_solution(arrayA, arrayB))
