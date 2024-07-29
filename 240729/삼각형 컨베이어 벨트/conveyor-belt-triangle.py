from collections import deque

n, t = map(int, input().split())

n_list = deque()

for _ in range(n):
    n_list.extend(list(map(int, input().split())))


for _ in range(t):
    n_list.appendleft(n_list.pop())

# print(n_list)

n_list = list(n_list)

for i in range(0, len(n_list), n):
        chunk = n_list[i : i + n]
        print(' '.join(map(str, chunk)))