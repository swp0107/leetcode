def twoSum(nums, target):
    # hash 2
    hash_nums = {}
    for index, num in enumerate(nums):
        another = target - num
        try:
            hash_nums[another]
            return [hash_nums[another], index]
        except KeyError:
            hash_nums[num] = index

nums = [3,2,4]
target = 6
print(twoSum(nums, target))
