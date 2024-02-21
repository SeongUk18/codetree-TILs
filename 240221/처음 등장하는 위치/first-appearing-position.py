from sortedcontainers import SortedDict 

n = int(input())
numbers = list(map(int, input().split()))

num_dic = SortedDict()

for i in range(len(numbers)):
    if numbers[i] in num_dic:
        continue
    else:
        num_dic[numbers[i]] = i + 1

for k, v in num_dic.items():
    print("{} {}".format(k, v))