class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # # method 1
        # if x % 10 == x:
        #     return True
        # else:
        #     if str(x) == str(x)[::-1]:
        #         return True
        # return False

        # method 2
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            temp = 0
            while x > temp:
                temp = temp * 10 + x % 10
                x = x // 10
        return x == temp or x == temp // 10


obj = Solution()
print(obj.isPalindrome(0))
