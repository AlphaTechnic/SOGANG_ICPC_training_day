"""
input :
2 3 5

output :
15
"""

import sys
from itertools import combinations
sys.stdin = open("input.txt")
input = sys.stdin.readline

data = list(map(int, input().rstrip().split()))

odd = []
even = []
for i in data:
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)
odd.sort(reverse=True)
even.sort(reverse=True)
new_set = odd + even
val1 = new_set[0]

data2 = []
odd = []
even = []
for x, y in combinations(data, 2):
    i = x*y
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)
odd.sort(reverse=True)
even.sort(reverse=True)
new_set = odd + even
val2 = new_set[0]

val3 = 1
for i in data:
    val3 *= i

final_data = [val1, val2, val3]
odd = []
even = []
for i in final_data:
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)
odd.sort(reverse=True)
even.sort(reverse=True)
new_set = odd + even
val1 = new_set[0]
print(new_set[0])