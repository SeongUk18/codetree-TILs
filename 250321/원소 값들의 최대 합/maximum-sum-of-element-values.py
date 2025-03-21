n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = float('-inf')
n_dict = {k + 1 : arr[k] for k in range(n)}
for i in range(1, n + 1):
    start = i
    point = 0
    
    for _ in range(m):
        next_s = n_dict[start]
        # print(n_dict)
        # print(next_s)

        point += next_s
        start = next_s
        
    max_sum = max(max_sum, point)

print(max_sum)