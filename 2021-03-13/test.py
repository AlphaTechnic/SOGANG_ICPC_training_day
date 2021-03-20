"""
input:
37 4
31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
"""
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 1
num = K
while num < N:
    num += K-1
    cnt += 1
print(cnt)
