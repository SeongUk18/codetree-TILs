n, t = map(int, input().split())

num_list = list(map(int, input().split()))

answer = 0

for i in range(len(num_list)):
    if i == 0:
        number = num_list[i]
        cnt = 0
    elif num_list[i] <= t:
        continue
    elif num_list[i] > number:
        cnt += 1
    else:
        cnt = 0
    number = num_list[i]
    answer = max(cnt, answer)


if answer == 0 and num_list[0] > t:
    print(1)
else:
    print(answer)