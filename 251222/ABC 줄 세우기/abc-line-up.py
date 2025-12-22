n = int(input())
arr = list(input().split())

# Please write your code here.
final = []
answer = 0

for i in range(65, 65 + n):
    final.append(chr(i))

# print(final)

for i in range(n):
    if final[i] != arr[i]:
        find = 0
        for j in range(i + 1, n):
            if arr[j] == final[i]:
                find = j
                break
        arr[i], arr[find] = arr[find], arr[i]
        answer += 1

print(answer)        