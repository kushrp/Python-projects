class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for c in range(-1,-len(s)-1,-1):
            print(s[c])
            ans+=s[c]
        print(ans)

s = Solution()
print(s.reverseString("whatup"))



