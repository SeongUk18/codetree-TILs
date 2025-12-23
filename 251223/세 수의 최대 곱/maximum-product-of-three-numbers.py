n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

max_num = max((arr[-1]* arr[-2]*arr[-3]),arr[-1]*arr[0]*arr[1])
print(max_num)