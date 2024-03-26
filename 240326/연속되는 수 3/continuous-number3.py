n = int(input())

cnt = 0
answer = 0
def check(number):
    if number > 0:
        flag = True
    else:
        flag = False
    return flag

for i in range(n):
    number = int(input())

    if i == 0:
        cnt = 1
        flag = check(number)
    else:
        if flag == check(number):
            cnt += 1
            flag = check(number)
        else:
            cnt = 1
            flag = check(number)
    
    answer = max(answer, cnt)

print(answer)