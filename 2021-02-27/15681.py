import sys

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

res = [0 for _ in range(N + 1)]
adj = [[] for _ in range(N + 1)]


def dfs(now):
    res[now] = 1
    for nxt in adj[now]:
        if res[nxt] == 0:
            dfs(nxt)
            res[now] += res[nxt]


for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dfs(R)
for _ in range(Q):
    q = int(input())
    print(res[q])

