"""
input:
7
0 5 0 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 1 0 0
0 0 0 0 0 2 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""
import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

pos_other = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 5:
            pos_prof = (r, c)
        elif board[r][c] == 1:
            pos_other.append((r, c))
        elif board[r][c] == 2:
            pos_student = (r, c)

if math.sqrt((pos_prof[0] - pos_student[0]) ** 2 + (pos_prof[1] - pos_student[1]) ** 2) < 5:
    print(0)
    exit()

min_r, min_c, max_r, max_c = min(pos_prof[0], pos_student[0]), min(pos_prof[1], pos_student[1]), \
                             max(pos_prof[0], pos_student[0]), max(pos_prof[1], pos_student[1])

cnt_other = 0
for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
        if board[r][c] == 1:
            cnt_other += 1

if cnt_other >= 3:
    print(1)
else:
    print(0)
