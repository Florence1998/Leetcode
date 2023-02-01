nums = [3, 7, 5]
count = len(nums)
for i in range(1, count):
    for j in range(0, count - i):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)
