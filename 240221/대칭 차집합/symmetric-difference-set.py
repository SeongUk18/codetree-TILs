n, m = map(int, input().split())

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

answer = (set1 - set2) | (set2 - set1)
print(len(answer))