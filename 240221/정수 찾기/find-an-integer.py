n = input()

num_set = set(map(int, input().split()))

m = input()

num_list = list(map(int, input().split()))

for i in num_list:
    if i in num_set:
        print(1)
    else:
        print(0)