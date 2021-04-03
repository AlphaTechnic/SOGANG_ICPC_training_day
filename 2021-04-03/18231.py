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
graph = [[] for _ in range(V+1)]
DEAD = dict()
for i in range(1, V+1):
    DEAD[i] = False

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

num_of_dead = int(input())
dead_list = list(map(int, input().split()))
for dead_num in dead_list:
    DEAD[dead_num] = True

solution = set()
ans = []
for dead_num in dead_list:
    for i in graph[dead_num]:
        if DEAD[i] == False:
            break
    else:
        ans.append(dead_num)
        solution.add(dead_num)
        solution = solution.union(set(graph[dead_num]))

ans = list(set(ans))
ans.sort()

if len(ans) == 0:
    print(-1)
else:
    for dead_num in dead_list:
        if dead_num not in solution:
            print(-1)
            exit()
    print(len(ans))
    for num in ans:
        print(num, end=' ')