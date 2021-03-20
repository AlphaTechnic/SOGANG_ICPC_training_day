import sys
sys.stdin = open("input.txt", "r")

N = int(input())

for i in range(1, min(N, 10**5)):
    A = i; A_str = str(i)
    B = N - i; B_str = str(N - i)
    union_str = A_str + B_str

    tmp = ''
    for j in union_str:
        if j not in tmp:
            tmp += j
        else:
            break
    else:
        print(N - i, "+", i)
        exit(0)
print(-1)