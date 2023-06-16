class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            f,l=i+1,len(nums)-1
            while f<l:
                if nums[i]+nums[f]+nums[l]==0:
                    lst=[nums[i],nums[f],nums[l]]
                    if lst not in ans:
                        ans.append([nums[i],nums[f],nums[l]])
                    f=f+1
                    l=l-1
                elif nums[i]+nums[f]+nums[l]<0:
                    f=f+1
                else:
                    l=l-1
        return ans
