n = int(input())
a = list(map(int, input().split()))

answer = 0

for i in range(n):
    for k in range(min(a), max(a)):
        diff = k - a[i]

        if (diff + k) in a and diff != 0:
            # print(a[i], diff, diff + k, k)
            answer += 1
    

print(answer // 2)
