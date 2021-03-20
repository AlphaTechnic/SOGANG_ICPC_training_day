import sys
sys.stdin = open("input.txt", "r")
import collections

node = [[] for _ in range(101)]

def bfs(n):
    chk[n] = 0
    queue = collections.deque([])
    queue.append(n)
    while len(queue) != 0:
        i = queue[0]
        queue.popleft()
        for j in range(len(node[i])):
            if chk[node[i][j]] == -1:
                queue.append(node[i][j])
                chk[node[i][j]] = chk[i] + 1


N, K = map(int, input().split())
for _ in range(K):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

flag = 0
for i in range(1, N+1):
    if flag == 1:
        break
    chk = [-1 for _ in range(101)]
    bfs(i)
    for j in range(1, N+1):
        if chk[j] == -1 or chk[j] > 6:
            print("Big World!")
            flag = 1
            break

if flag:
    pass
else:
    print("Small World!")