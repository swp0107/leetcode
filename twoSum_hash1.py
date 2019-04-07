def twoSum(nums, target):
# hash 1
    hash_nums = {}
    for index, num in enumerate(nums):
        try:
            hash_nums[num].append(index)
        except KeyError:
            hash_nums[num] = [index]
        print (hash_nums)
        for index, num in enumerate(nums):
            another = target - num
            try:
                candicate = hash_nums[another]
                print(candicate)
                if another == num:
                    print("yes")
                    print(len(candicate))
                    if len(candicate) > 1:
                        return candicate
                    else:
                        continue
                else:
                    return [index, candicate[0]]
            except KeyError:
                pass

nums = [3,2,4]
target = 6
print(twoSum(nums, target))
