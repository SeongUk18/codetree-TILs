from itertools import product

k, n = map(int, input().split())

num = list(range(1, k + 1))

# print(num)
n_list = list(product(num, repeat = n))

for i in n_list:
    for j in i:
        print(j, end=" ")
    print()