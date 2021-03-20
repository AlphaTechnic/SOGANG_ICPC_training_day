import sys
sys.stdin = open("input.txt", "r")


def get_gcd(N, M):
    while N % M != 0:
        mod = M
        M = N % M
        N = mod
    return M

N, M = map(int, input().split(':'))

G = get_gcd(N, M)
print('%d:%d' % (N//G, M//G))

