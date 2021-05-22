"""
input :
9
1 2 3 3 4 1 10 8 1
5
1 3
2 5
4 7
9 9
5 9

output :
0
0
1
0
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
data = ['_'] + list(map(int, input().rstrip().split()))
decrease = [0 for _ in range(N + 1)]
Q = int(input())

for i in range(1, N):
    if data[i] > data[i+1]:
        decrease[i] = 1

dec_accumulated = []
tot = 0
for i in decrease:
    tot += i
    dec_accumulated.append(tot)

for _ in range(Q):
    l, r = map(int, input().rstrip().split())
    print(dec_accumulated[r-1] - dec_accumulated[l-1])

dp = [0 for _ in range(N)]
for 