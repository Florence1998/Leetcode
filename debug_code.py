nums = [3, 2, 4]
target = 6
for num_index1 in range(0, len(nums)):
    num2 = target - nums[num_index1]
    if (num2 in nums) & (num_index1 < nums.index(nums)):
        res = [num_index1, nums.index(num2)]
        print(res)
