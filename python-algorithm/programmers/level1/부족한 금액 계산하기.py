def solution(price, money, count):
    sum = 0
    for c in range(1, count + 1):
        sum += price * c

    if sum < money:
        return 0
    else:
        return sum - money
