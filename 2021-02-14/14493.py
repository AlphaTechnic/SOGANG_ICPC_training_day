import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N = int(input())

ans = 0
for i in range(N):
    term, active = map(int, input().split())
    mod = ans % (term + active)

    if mod < active:
        ans += active - mod + 1
    else:
        ans += 1

print(ans)