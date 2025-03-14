n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
x_set = set()
flag = False
for i in range(len(x)):
    count = 0
    y_set = set()
    if x[i] not in x_set:
        x_set.add(x[i])
    count = len(x_set)

    for j in range(len(y)):
        if x[j] in x_set:
            continue
        else:
            if y[j] not in y_set:
                y_set.add(y[j])
                count += 1
        if count > 3:
            break
    
    if count <= 3:
        flag = True

y_set = set()
for i in range(len(x)):
    count = 0
    x_set = set()
    if y[i] not in y_set:
        y_set.add(y[i])
    count = len(y_set)

    for j in range(len(x)):
        if y[j] in y_set:
            continue
        else:
            if x[j] not in x_set:
                x_set.add(x[j])
                count += 1
        if count > 3:
            break
    
    if count <= 3:
        flag = True


if flag:
    print(1)
else:
    print(0)