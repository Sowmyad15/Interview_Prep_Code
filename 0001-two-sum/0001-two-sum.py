class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in d:
                return [d[compliment],i]
            d[nums[i]]=i
            
        