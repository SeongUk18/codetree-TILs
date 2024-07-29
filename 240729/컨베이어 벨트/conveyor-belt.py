from collections import deque

n, t = map(int, input().split())

n_list = deque()

for _ in range(2):
    n_list.extend(list(map(int, input().split())))

# print(n_list)
for _ in range(t):
    n_list.appendleft(n_list.pop())

n_list = list(n_list)
# print(n_list)
for i in range(n):
    print(n_list[i], end=" ")
    
print()

for i in range(n, len(n_list)):
    print(n_list[i], end=" ")