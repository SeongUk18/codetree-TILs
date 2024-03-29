n = int(input())

num = int(input())
cnt_list = []
cnt = 1

for _ in range(n-1):
    number = int(input())
    if number > num:
        cnt += 1
        num = number
        
    else:
        cnt = 1
        num = number
    cnt_list.append(cnt)
cnt_list.append(cnt)


print(max(cnt_list))