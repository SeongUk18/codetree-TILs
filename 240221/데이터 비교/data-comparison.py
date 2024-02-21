n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int, input().split()))

answer = []

for i in arr_2:
    if i in arr_1:
        answer.append(1)
    else:
        answer.append(0)

for j in answer:
    print(j, end=" ")