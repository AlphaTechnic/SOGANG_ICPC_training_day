import sys
sys.stdin = open("input.txt", "r")

mod = 1000000009
N = int(input())
ans = 1
for i in range(N):
    ans = ans*(2*i+1) % mod

print(ans)
