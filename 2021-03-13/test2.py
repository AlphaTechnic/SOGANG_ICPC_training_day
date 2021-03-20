"""
input:
4
12 0
10 14
4 20
5 2147483648
"""

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    special, normal = map(int, input().split())

    cnt = min(special // 5, normal // 7)
    s_margin, n_margin = special - cnt * 5, normal - cnt * 7
    if s_margin >= 5 and s_margin + n_margin >= 12:  # 남는 쿠폰 소모
        cnt += 1

    print(cnt)
print(4 << 1)
