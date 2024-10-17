class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        d={}
        length=0
        for r in range(len(s)):
            c=s[r]
            if c in d and d[c]>=l:
                l=d[c]+1
            d[c]=r
            length=max(length,r-l+1)
        return length
