"""
input:
5 3
1 2
3 2
5 4
4
1 2 4 5
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

num_of_dead = int(input())
destroyed_cities = set(map(int, input().split()))
alive_cities = {i for i in range(1, V+1)} - destroyed_cities

destroyed_accumulated = set()
ans = set()
for destroyed_city in destroyed_cities:
    for adj in graph[destroyed_city]:
        if adj in alive_cities:
            break
    else:  # 인접한 노드 중 alive가 없으니, 폭탄이 떨어진 도시라고 해도 됨
        ans.add(destroyed_city)
        destroyed_accumulated.add(destroyed_city)  # 폭탄이 떨어진 도시와
        destroyed_accumulated = destroyed_accumulated.union(set(graph[destroyed_city]))  # 인접한 도시를 기록

ans = list(ans)
ans.sort()
empty_set = destroyed_cities - destroyed_accumulated  # destroyed_accumulated가 문제에서 제시한 모든 파괴도시를 cover 해야함.

if len(empty_set) != 0:
    print(-1)
else:
    print(len(ans))
    for city in ans:
        print(city, end=' ')
