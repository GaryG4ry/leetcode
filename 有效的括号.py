class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dic = {'}': '{', ')': '(', ']': '['}
        temp = []
        length = len(s)
        if length == 0 or length % 2 != 0:
            return False
        for i in range(length):
            if s[i] in dic.values():
                temp.append(s[i])
            else:
                if not temp or temp.pop() != dic[s[i]]:
                    return False
        return True


print(Solution().isValid(''))
