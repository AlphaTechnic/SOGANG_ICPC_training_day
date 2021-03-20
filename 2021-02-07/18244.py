import sys
sys.stdin = open("input.txt", "r")

mod = 1000000007
N = int(input())
a = [[], [], [], [], []]
b = [a for _ in range(N+1)]
dp = [b for _ in range(11)]

for i in range(10):
    dp[i][1][0] = 1

Sum = 0

for i in range(2, N+1):
    for j in range(10):
        if j!=9:
            dp[j][i][1] += (dp[j+1][i-1][0] % mod + dp[j+1][i-1][3] % mod + dp[j+1][i-1][4] % mod) % mod
            dp[j][i][2] += (dp[j + 1][i - 1][1] % mod) % mod

        if j!=0:
            dp[j][i][3] += (dp[j - 1][i - 1][0] % mod + dp[j - 1][i - 1][1] % mod + dp[j - 1][i - 1][2] % mod) % mod
            dp[j][i][4] += (dp[j - 1][i - 1][3] % mod) % mod


for i in range(10):
    for k in range(5):
        Sum = (Sum % mod + (dp[i][N][k] % mod)) % mod