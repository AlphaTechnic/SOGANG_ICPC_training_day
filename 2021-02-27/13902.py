import sys
sys.stdin = open("input.txt", "r")

MAX = 999999999

N, M = map(int, input().split())
units = list(map(int, input().split()))

for i in range(M):
    for j in range(i+1, M):
        units.append(units[i] + units[j])

units = sorted(set(units))

dp = [0 for _ in range(10001)]

for i in range(1, N+1):
    dp[i] = MAX
    for j in range(len(units)):
        if i - units[j] >= 0:
            dp[i] = min(dp[i], dp[i-units[j]]+1)
        else:
            break

if dp[N] == MAX:
    print(-1)
else:
    print(dp[N])
