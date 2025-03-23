N = int(input())
adjacent = list(map(int, input().split()))


for i in range(1, N + 1):
    a = i
    num_list = [a]
    for num in adjacent:
        if num - a > 0 and (num - a) not in num_list:
            # print(num_list)
            # print(num, a, num - a)
            num_list.append(num - a)
            a = num - a
    # print(num_list)
    if len(num_list) == N:
        for n in num_list:
            print(n, end=" ")
        break
