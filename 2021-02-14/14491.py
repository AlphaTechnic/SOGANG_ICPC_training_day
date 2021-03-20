import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
T = int(input())

st = []
while T != 0:
    st.append(T % 9)
    T = T // 9

st.reverse()
for i in st:
    print(i, end='')