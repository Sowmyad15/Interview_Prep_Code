"""345. Reverse Vowels of a String
Easy
3.5K
2.4K
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        v="AEIOUaeiou"
        l=0
        r=len(s)-1
        while l<r:
            if s[l] not in v and s[r] not in v:
                l=l+1
                r=r-1
            elif s[l] not in v:
                l=l+1
            elif s[r] not in v:
                r=r-1
            else:
                s[l],s[r]=s[r],s[l]
                l=l+1
                r=r-1
        return "".join(s)
    
