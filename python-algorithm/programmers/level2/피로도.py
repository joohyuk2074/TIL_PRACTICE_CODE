max = -1

# ABC 이렇게 있다면
# ABC ACB BAC BCA CAB CBA 이렇게 던전을 갈 수 있다.
#
# 모두 탐색을 하면서 visited의 최대값을 구하면 된다.
#
# 무식하긴한데 방법이 이거말곤 떠오르지 않네요 ㅡ.ㅡ

def solution(k, dungeons):
    answer = -1

    visited = [False for _ in range(0, len(dungeons))]
    dfs(k, dungeons, visited)

    return answer

def dfs(k, dungeons, visited):



k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
