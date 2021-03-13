"""
4
123 456 999 73
6
111 5 3
456 -1 -1
123 4 59
73 6 0
520 -1 -1
999 6 0
"""

import sys
from collections import OrderedDict
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 10**9

T = int(input())
for _ in range(T):
    NUM_OF_STUDENTS = int(input())
    students = list(map(int, input().split()))
    students_dict = OrderedDict()
    for i in students:
        students_dict[i] = INF

    NUM_OF_PARTICIPANTS = int(input())
    for _ in range(NUM_OF_PARTICIPANTS):
        num, h, m = map(int, input().split())
        if num in students_dict:
            if h != -1:
                students_dict[num] = 60 * h + m

    min_val = INF
    winner = -1
    cnt = 0
    for key, val in students_dict.items():
        if val <= 360:
            cnt += 1
        if val < min_val:
            winner, min_val = key, val

    print(winner, cnt)