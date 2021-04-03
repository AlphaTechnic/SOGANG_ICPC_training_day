"""
input :
8
5 2 -1 9 9 9 9 1

output :
3
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e10)

N = int(input())
num_list = list(map(int, input().split()))

l = 0
r = N - 1
l_min = INF
r_min = INF
while num_list[l] != -1:
    if l_min > num_list[l]:
        l_min = num_list[l]
    l += 1
while num_list[r] != -1:
    if r_min > num_list[r]:
        r_min = num_list[r]
    r -= 1

print(l_min + r_min)
