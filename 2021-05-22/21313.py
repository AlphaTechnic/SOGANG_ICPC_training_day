"""
input :
4

output :
1 2 1 2
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
ans = ""
for _ in range(N // 2):
    ans += "1 "
    ans += "2 "

if N % 2 == 0:
    ans = ans[:-1]
if N % 2 == 1:
    ans += "3"
print(ans)