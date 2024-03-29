n, t = map(int, input().split())

num_list = list(map(int, input().split()))

answer = 0
cnt = 0

for i in range(len(num_list)):
    if i == 0 and num_list[i] > t:
        cnt += 1
    elif i >= 1 and num_list[i] > t and num_list[i] > num_list[i - 1]:
        cnt += 1
    else:
        cnt = 0
    answer = max(cnt, answer)


print(answer)