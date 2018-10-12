class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        if length == 0:
            return 0
        # # use python package
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1

        # use str slice
        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i
        return -1
print(Solution().strStr(haystack="hello", needle="ll"))
