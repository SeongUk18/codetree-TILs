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
        for j in range(i, n):
            if arr[j] == final[i]:
                find = j
                break

        for j in range(find, i, -1):
            answer += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            # print(arr)
                
print(answer)        