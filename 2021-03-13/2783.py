"""
input :
5 100
3
4 100
3 100
7 100
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

data = []
price, gram = map(int, input().split())
price_per_gram = price / gram
data.append([price_per_gram, price, gram])

N = int(input())
for _ in range(N):
    price, gram = map(int, input().split())
    price_per_gram = price / gram
    data.append([price_per_gram, price, gram])

min_per_gram, _, _ = min(data)
print(format(min_per_gram*1000, ".2f"))