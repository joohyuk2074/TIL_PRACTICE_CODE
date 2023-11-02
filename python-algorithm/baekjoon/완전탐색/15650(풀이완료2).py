def recursive(start, answer, cnt):
    if cnt >= m:
        print(*answer, sep=' ')
        return

    for i in range(start, n + 1):
        answer.append(i)
        recursive(i + 1, answer, cnt + 1)
        answer.remove(i)


n, m = map(int, input().split())
recursive(1, answer=[], cnt=0)
