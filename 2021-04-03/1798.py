"""
input :
3.0 4.0 2.0 0.0 4.0 0.0
3.0 4.0 2.0 90.0 4.0 0.0
6.0 8.0 2.14 75.2 9.58 114.3
3.0 4.0 5.0 0.0 5.0 90.0

ouput :
2.00
3.26
7.66
4.54
"""

import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

for line in sys.stdin:
    r, h, d1, a1, d2, a2 = map(float, line.rstrip().split())
    R = math.sqrt(r ** 2 + h ** 2)
    Arc = 2 * math.pi * r
    A = Arc / R

    target_A = A * abs(a2 - a1) / 360
    if target_A > A / 2:
        target_A = A - target_A
    print("%0.2f" % math.sqrt(d1 ** 2 + d2 ** 2 - 2 * d1 * d2 * math.cos(target_A)))