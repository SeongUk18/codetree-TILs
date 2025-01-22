from collections import deque

n = int(input())
a = [int(input()) for _ in range(n)]

q = deque(a)

min_move = float('inf')
for _ in range(n):
    move = 0
    for i in range(n):
        move += i * q[i]
    
    room = q.popleft()
    q.append(room)
    min_move = min(move, min_move)

print(min_move)