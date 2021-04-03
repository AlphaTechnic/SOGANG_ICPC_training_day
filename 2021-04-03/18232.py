"""
input :
5 1
1 5
1 4

output :
2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # heqp에서 꺼냈는데 이미 처리된 놈이면 continue
        if distance[now] < dist:
            continue

        for nxt, weight in graph[now]:
            cost = distance[now] + weight
            if distance[nxt] > cost:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]
S, End = map(int, input().split())

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
for i in range(1, V):
    graph[i].append((i + 1, 1))
    graph[i + 1].append((i, 1))

dijkstra(S)

print(distance[End])
