n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0
covered = -1

for i in range(n):
    # 해당 위치에 사람이 살고 있고(1), 아직 커버되지 않은 경우
    if arr[i] == 1 and i > covered:
        answer += 1
        covered = i + 2 * m

print(answer)