def cf(n):
    a = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(n // i)
            a.append(i)
    return len(set(a))
