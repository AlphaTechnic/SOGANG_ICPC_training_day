"""
input :
4 5 20
3 5 2 1 4
1 8 2 5 8
1 5 2 3 3
1 1 8 9 9

output:
2 5
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e10)

R, C, K = map(int, input().split())
board = [[0 for _ in range(C)]]
for _ in range(R):
    arr = list(map(int, input().split()))
    board.append(arr)
total_list = [0] + [0 for _ in range(R)]

c = 0
escape_flag = 0
loop_cnt = 0
while True:
    loop_cnt += 1
    for r in range(1, R + 1):
        total_list[r] += board[r][c]
        if total_list[r] >= K:
            escape_flag = 1
            break
    if escape_flag == 1:
        break
    c = (c + 1) % C

print(r, loop_cnt)
