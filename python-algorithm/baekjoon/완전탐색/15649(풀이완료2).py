def recursive(answer, cnt, check):
    if cnt >= m:
        print(*answer, sep=' ')
        return

    for i in range(1, n + 1):
        if check[i] is False:
            check[i] = True
            answer.append(i)
            recursive(answer, cnt + 1, check)
            answer.remove(i)
            check[i] = False


n, m = map(int, input().split())
checks = [False] * (n + 1)
recursive(answer=[], cnt=0, check=checks)
