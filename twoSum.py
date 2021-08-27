class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            sub = target - num
            if num not in dic.keys():
                dic[sub] = i
            else:
                return [dic[num], i]


ob = Solution()
result = ob.twoSum([2, 7, 11, 15], 9)
print(result)
