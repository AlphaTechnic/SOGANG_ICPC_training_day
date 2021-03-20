import sys
sys.stdin = open("input.txt", "r")

N = int(input())
dep_list = list(map(int, input().split()))
dep_cnt = [0 for _ in range(30)]
binary_tree = [[_, _] for _ in range(30)]
dep = [[_, _] for _ in range(30)]
f = 1
dep[0].append(0)
for ind, d in enumerate(dep_list):
    if dep_cnt[d - 1]*2 < dep_cnt[d] + 1:
        break
    else:
        prev = dep[d-1][0]
        if binary_tree[prev][0] == False:
            binary_tree[prev][0] = ind
        else:
            binary_tree[prev][1] = ind
            del(dep[d-1][0])
        dep[d].append = ind
    dep_cnt[dep_list] += 1

print(binary_tree)