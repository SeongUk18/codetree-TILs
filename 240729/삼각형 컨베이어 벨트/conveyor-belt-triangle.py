from collections import deque

n, t = map(int, input().split())

n_list = deque()

for _ in range(n):
    n_list.extend(list(map(int, input().split())))


for _ in range(t):
    n_list.appendleft(n_list.pop())

# print(n_list)

for i in range(n):
    print(n_list[i], end=" ")
print()
for i in range(n, len(n_list) - n):
    print(n_list[i], end=" ")
print()
for i in range(2 * n, len(n_list)):
    print(n_list[i], end=" ")