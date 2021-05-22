"""
input :
1 2
2 3
3 4
4 5
3 7
4 9
6 7
7 8
9 8
9 10
10 11
12 11

output :
7
"""
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
graph = [[] for _ in range(13)]
for _ in range(12):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

deg3 = []
for i, nodes in enumerate(graph):
    if len(nodes) == 3:
        deg3.append(i)

ans_set = {1, 2, 3}
ans = 0
for i in deg3:
    data_set = set()
    for j in graph[i]:
        data_set.add(len(graph[j]))
    if data_set == ans_set:
        ans = i
print(ans)
