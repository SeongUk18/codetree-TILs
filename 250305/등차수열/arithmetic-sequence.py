n = int(input())
a = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        # K를 계산
        k = (a[i] + a[j]) // 2
        
        # 등차수열 조건 확인
        if (a[j] - k) == (k - a[i]):
            answer += 1

print(answer)