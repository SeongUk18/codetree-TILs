n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
sorted_a = sorted(list(set(a)))

if len(sorted_a) == 1:
    print(-1)
    exit()

find = sorted_a[1]
# print(find)

flag = 0
answer = 0

for i in range(n):
    if a[i] == find and flag == 0:
        answer = i + 1
        flag += 1
    elif a[i] == find:
        flag += 1

# print(flag)
if flag >= 2:
    print(-1)
else:
    print(answer)