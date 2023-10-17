n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    a, b, c = input().split()
    # 아스키코드!
    a = ord(a)
    b = ord(b)
    c = ord(c)

    graph[a].append(b)
    graph[a].append(c)


def pre_order(node):
    if node == 46:
        return

    print(chr(node), end="")
    pre_order(graph[node][0])
    pre_order(graph[node][1])


def post_order(node):
    if node == 46:
        return

    post_order(graph[node][0])
    post_order(graph[node][1])
    print(chr(node), end="")


def in_order(node):
    if node == 46:
        return

    post_order(graph[node][0])
    print(chr(node), end="")
    post_order(graph[node][1])


pre_order(65)
print()
in_order(65)
print()
post_order(65)
print()
