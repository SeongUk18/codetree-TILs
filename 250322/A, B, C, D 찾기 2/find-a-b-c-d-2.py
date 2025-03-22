nums = list(map(int, input().split()))

nums.sort()

A = nums[0]

B = nums[1]

for i in range(2, len(nums)):
    if nums[i] < A + B:
        C = nums[i]
        break
    else:
        C = nums[i]
        break

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