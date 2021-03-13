"""
input:
20181208
"""
import sys
import collections as col

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

candi = ['2', '0', '1', '8']
N_list = list(input().rstrip())
cnt_data = dict(col.Counter(N_list))


def solve():
    type = 8
    for key, val in cnt_data.items():
        if key not in candi:
            type = 0
            return type

    if len(cnt_data.keys()) != 4:
        type = 1
        return type

    tmp = cnt_data['2']
    for key, val in cnt_data.items():
        if val != tmp:
            type = 2
            return type
    return type


print(solve())
