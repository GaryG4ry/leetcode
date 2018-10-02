class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # # method 1
        # l = list(s)
        # num = 0
        # for i in range(len(l)):
        #     num = num_dict.get(l[i]) + num
        #     if i != len(l)-1:
        #         if (l[i] == 'I' and l[i + 1] == 'V') or (l[i] == 'I' and l[i + 1] == 'X'):
        #             num = num - 2
        #         elif (l[i] == 'X' and l[i + 1] == 'L') or (l[i] == 'X' and l[i + 1] == 'C'):
        #             num = num - 20
        #         elif (l[i] == 'C' and l[i + 1] == 'D') or (l[i] == 'C' and l[i + 1] == 'M'):
        #             num = num - 200
        # return num

        # method 2
        num = 0
        for i in range(len(s) - 1):
            if num_dict[s[i]] < num_dict[s[i + 1]]:
                num = num - num_dict[s[i]]
            else:
                num = num + num_dict[s[i]]
        return num + num_dict[s[-1]]


obj = Solution()
print(obj.romanToInt('MCMXCIV'))
