class Solution:
    def searchRange(self, nums, target: int):
        if (len(nums) == 1):
            if (target in nums):
                return([0,0])
            else:
                return([-1,-1])
        if target in nums:
            first = nums.index(target)
            i = first+1
            try:
                while (nums[first] == nums[i]):
                    i += 1
                last = i-1
            except:
                last = i-1
        else:
            return([-1, -1])
        return([first, last])

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target))
nums = [5,7,7,8,8,10]
target = 6
print(s.searchRange(nums, target))
nums = [1]
target = 1
print(s.searchRange(nums, target))
nums = [2,2]
target = 2
print(s.searchRange(nums, target))
