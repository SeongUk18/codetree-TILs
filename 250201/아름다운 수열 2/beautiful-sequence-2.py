N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
B = sorted(B)
for i in range(N - M + 1):
    new_arr = sorted(A[i:i + M])
    # print(new_arr)
    new_arr = sorted(new_arr)
    if new_arr == B:
        answer += 1

print(answer)