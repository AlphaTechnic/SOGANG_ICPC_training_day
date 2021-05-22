"""
input :
5
1 2
2 3
4 5
6 7
4

output :
5
"""

import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
small_jump = ['_']
big_jump = ['_']
is_used = True

for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    small_jump.append(a)
    big_jump.append(b)
very_big_jump = int(input())

tot = 10**9
def dfs(ind, is_used, accumul):
    global tot
    if ind == N:
        tot = min(tot, accumul)

    if ind + 1 <= N:
        dfs(ind + 1, is_used, accumul + small_jump[ind])
    if ind + 2 <= N:
        dfs(ind + 2, is_used, accumul + big_jump[ind])
    if ind + 3 <= N:
        dfs(ind+3, 1, accumul + very_big_jump)

dfs(1, 0, 0)
print(tot)