import sys
sys.stdin = open("input.txt", "r")

MAX = 512
input = sys.stdin.readline

graph = [[] for _ in range(MAX)]
B = [-1 for _ in range(MAX)]
choose = [0 for _ in range(MAX)]
not_choose = [0 for _ in range(MAX)]


def dfs(x):
    visited[x] = True
    for v in graph[x]:
        if B[v] == -1 or visited[B[v]] is False and dfs(B[v]):
            B[v] = x
            return True
    return False


optionA = []
optionB = []
n, m, k = map(int, input().split())
for b in range(k):
    ni, mi, c = map(int, input().split())

    if c == 0:
        optionA.append(b)
        choose[b] = mi
        not_choose[b] = ni
    else:
        optionB.append(b)
        choose[b] = ni
        not_choose[b] = mi

for b in optionB:
    for a in optionA:
        if choose[a] == not_choose[b] or choose[b] == not_choose[a]:
            graph[b].append(a)

print(optionB)

ans = 0
for b in optionB:
    visited = [False for _ in range(MAX)]
    if dfs(b):
        ans += 1

print(ans)