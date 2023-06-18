from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=Counter(nums)
        print(x.items())
        for i in x.keys():
            if x[i]==1:
                return i

        return 0
