n = int(input())
h = [int(input()) for _ in range(n)]

max_count = 0
for i in range(1, max(h) + 1):
    count = 0
    flag = False
    for j in range(n):
        if h[j] > i:
            flag = True
        
        if h[j] <= i:
            if not flag:
                continue
            else:
                count += 1
                flag = False
    if flag:
        count += 1
    
    max_count = max(max_count, count)


print(max_count)
