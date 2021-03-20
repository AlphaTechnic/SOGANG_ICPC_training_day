import sys
sys.stdin = open("input.txt", "r")

import heapq

mod = 1000000009
MAX = 100001
INF = 100000000000000000
input = sys.stdin.readline

dp = [0 for _ in range(MAX)]
dist = [INF for _ in range(MAX)]
adj = [[] for _ in range(MAX)]


N, M, S, E = map(int, input().split())
for i in range(M):
    node1, node2, cost = map(int, input().split())
    adj[node1].append([node2, cost])
    adj[node2].append([node1, cost])

pq = []
heapq.heappush(pq, [0, S])
dist[S] = 0
dp[S] = 1

while len(pq) != 0:
    cur_dist, cur = pq[0]
    heapq.heappop(pq)

    if dist[cur] < cur_dist:
        continue

    for nxt, nxt_dist in adj[cur]:
        if dist[nxt] < cur_dist + nxt_dist:
            continue
        if dist[nxt] == cur_dist + nxt_dist:
            dp[nxt] += dp[cur]
            dp[nxt] %= mod
        else: # dist[nxt] > cur_dist + nxt_dist
            dist[nxt] = cur_dist + nxt_dist
            heapq.heappush(pq, [cur_dist + nxt_dist, nxt])
            dp[nxt] = dp[cur] % mod

print(dp[E])
