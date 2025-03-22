nums = list(map(int, input().split()))

nums.sort()

A = nums[0]

B = nums[1]

if nums[2] == A + B:
    C = nums[3]
else:
    C = nums[2]

num_set = [A, B, C, A + B, A + C, B + C, A + B + C]
for i in nums:
    if i in num_set:
        num_set.remove(i)
        continue
    else:
        D = i
        break
# print(num_set)
# print(nums)
print(f"{A} {B} {C} {D}")