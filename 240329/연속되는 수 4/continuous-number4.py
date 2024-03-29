n = int(input())

num = int(input())
cnt_list = []
cnt = 0

for _ in range(n-1):
    number = int(input())
    if number > num:
        cnt += 1
        num = number
        cnt_list.append(cnt)
    else:
        cnt_list.append(1)
        num = number

print(max(cnt_list))