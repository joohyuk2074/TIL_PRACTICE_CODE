def recursive(index, idx_str, p, f, s, v, c):
    global min_price
    global min_price_idx_str

    if index == n:
        if p < mp or f < mf or s < ms or v < mv:
            return

        if min_price > c:
            min_price = c
            min_price_idx_str = idx_str
        return

    recursive(
        index + 1,
        idx_str + str(index + 1) + " ",
        p + inputs[index][0],
        f + inputs[index][1],
        s + inputs[index][2],
        v + inputs[index][3],
        c + inputs[index][4]
    )

    recursive(
        index + 1,
        idx_str,
        p,
        f,
        s,
        v,
        c
    )


n = int(input())
mp, mf, ms, mv = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(n)]
min_price = 20000
min_price_idx_str = ""

recursive(index=0, idx_str="", p=0, f=0, s=0, v=0, c=0)


if min_price == 20000:
    print("-1")
else:
    print(min_price)
    print(min_price_idx_str)
# print(*min_price_idx_arr)
