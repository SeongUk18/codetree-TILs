from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_num = float('-inf')
num = 0

for com in combinations(arr, 3):
    # print(com)
    num = com[0] * com[1] * com[2]
    max_num = max(max_num, num)

print(max_num)