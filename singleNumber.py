class Solution:
    def singleNumber(self, nums) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]


s = Solution()
a = [2,2,1,4,4,5,1,5,6]
print(s.singleNumber(a))
