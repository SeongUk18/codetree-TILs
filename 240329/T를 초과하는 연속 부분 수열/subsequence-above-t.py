n, t = map(int, input().split())

num_list = list(map(int, input().split()))

cnt = 0
cnt_list = []
number = num_list[0]
for i in num_list[1:]:
    if i > t and i > number:
        cnt += 1
    else:
        cnt = 1
    cnt_list.append(cnt)
    number = i
cnt_list.append(cnt)

print(max(cnt_list))