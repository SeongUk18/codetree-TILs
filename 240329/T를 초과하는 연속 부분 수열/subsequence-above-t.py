n, t = map(int, input().split())

num_list = list(map(int, input().split()))

answer = -1

for i in range(len(num_list)):
    if i == 0:
        number = num_list[i]
        cnt = 0
    elif num_list[i] > number and num_list[i] > t:
        cnt += 1
    else:
        cnt = 0
    number = num_list[i]
    answer = max(cnt, answer)


if answer == 1 and num_list[0] <= t:
    print(0)
else:
    print(answer)