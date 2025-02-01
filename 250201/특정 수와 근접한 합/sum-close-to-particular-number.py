N, S = map(int, input().split())
arr = list(map(int, input().split()))

num = sum(arr)

if S >= num:
    new_arr = sorted(arr)
    new_arr = new_arr[2:]
else:
    new_arr = sorted(arr)
    new_arr = new_arr[:-2]

print(abs(S - sum(new_arr)))