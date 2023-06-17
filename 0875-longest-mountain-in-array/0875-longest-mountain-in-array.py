class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        A=arr
        if len(A) < 3: return 0
        if len(set(A)) == 1: return 0
        res = 0
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                l = i - 1
                r = i + 1
                while l > 0 and A[l - 1] < A[l]:
                    l -= 1
                while r < len(A) - 1 and A[r + 1] < A[r]:
                    r += 1
                res = max(res, r - l + 1)
        return res