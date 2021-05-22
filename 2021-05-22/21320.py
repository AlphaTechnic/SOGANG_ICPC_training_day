"""
input :
4 1

output :
5
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MOD = 10**9 + 7

HIGH, S = map(int, input().rstrip().split())
dp = [0 for _ in range(HIGH + 5)]
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 4
for i in range(3, HIGH + 1):
    if i % 2 == 1:
        dp[i] = 2 * dp[i - 1] + 1
    else:
        dp[i] = dp[i - 2] + 4 ** (i // 2 - 1)

if HIGH % 2 != S % 2:
    print(dp[HIGH] % MOD)
else:
    print((dp[HIGH] - 1) % MOD)
