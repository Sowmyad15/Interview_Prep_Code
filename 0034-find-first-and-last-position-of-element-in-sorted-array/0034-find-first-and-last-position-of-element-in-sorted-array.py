class Solution(object):
    def searchRange(self, nums, target):
        def lower_bound(nums, target):
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>=target:
                    r=mid-1
                else:
                    l=mid+1
            return l

        def upper_bound(nums, target):
            l,r=0,len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return r

        left = lower_bound(nums, target)
        right = upper_bound(nums, target)
        if left <= right:
            return [left, right]
        
        return [-1, -1]