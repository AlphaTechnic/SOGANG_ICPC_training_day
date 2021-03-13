"""
input:
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

data = list(input().rstrip())
l_r_cnt = dict()
for i in range(65, 65 + 26):
    l_r_cnt[chr(i)] = [0, 0, 0]

for ind, ch in enumerate(data):
    l_r_cnt[ch][2] += 1
    if l_r_cnt[ch][2] == 1:
        l_r_cnt[ch][0] = ind
    elif l_r_cnt[ch][2] == 2:
        l_r_cnt[ch][1] = ind

cnt = 0
for s1, e1, _ in l_r_cnt.values():
    for s2, e2, _ in l_r_cnt.values():
        if s1 < s2 < e1 < e2:
            cnt += 1

print(cnt)
