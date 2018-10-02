class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0 or len(s) == 0:
            return False
        for i in range(len(s)//2):
            if s[i] == s[len(s) - i - 1]:
                continue
            else:
                return False
        return True


x = Solution()
print(x.isValid(''))
print(len(''))
