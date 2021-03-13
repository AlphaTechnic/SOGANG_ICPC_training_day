"""
input:
ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

data = list(input().rstrip())
chk = dict()
for i in range(65, 65 + 26):
    chk[chr(i)] = 0

cnt = 0
st = [data[0]]
chk[data[0]] += 1
for i in data[1:]:
    chk[i] += 1
    if len(st) == 0:
        st.append(i)
        continue

    if i == st[-1]:
        st.pop()
    else:
        if chk[i] == 1:
            st.append(i)
        elif chk[i] == 2:
            ind = st.index(i)
            cnt += len(st) - 1 - ind
            del st[st.index(i)]

print(cnt)
