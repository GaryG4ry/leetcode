class Solution:
    def reverse(self, x):
        """
        :param x: int
        :return: int type
        """
        HIGH_LIMIT = pow(2, 31) - 1
        LOW_LIMIT = pow(-2, 31)
        # 判断是不是个位数
        if x % 10 == x:
            return x
        elif x > 0:
            x = str(x)[::-1]
            x = int(x)
        else:
            x = str(x)[1:][::-1]
            x = int(x)
            x = -x
        if x > LOW_LIMIT and x < HIGH_LIMIT:
            return x
        else:
            return 0


a = Solution()
print(a.reverse(-10111))
