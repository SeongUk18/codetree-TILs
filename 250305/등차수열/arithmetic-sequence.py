n = int(input())
a = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        if (a[i] + a[j]) % 2 == 0:
            answer += 1

print(answer // 2)
