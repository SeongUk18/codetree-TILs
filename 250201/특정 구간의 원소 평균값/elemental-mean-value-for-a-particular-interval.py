n = int(input())
arr = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(1, n - i + 1):
        # print(arr[i:i + j])
        avg = sum(arr[i:i + j]) / len(arr[i:i + j])
        # print(avg)
        if avg in arr[i:i + j]:
            answer += 1

print(answer)