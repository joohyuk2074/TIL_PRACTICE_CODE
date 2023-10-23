n = int(input())
for _ in range(n):
    number = int(input())

    flag = True
    for i in range(2, 10 ** 6):
        if number % i == 0:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
