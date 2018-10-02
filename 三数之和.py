class Solution:

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
                    else:
                        continue

        for item in result:
            item.sort()

        temp = set(result)

        # for i in range(len(result)-1):
        #     for j in range(i + 1, len(result)):
        #         if result[i] == result[j]:
        #             result.remove(result[i])    # Bug here
        #         else:
        #             continue

        return temp


x = Solution()
print((x.threeSum(nums=[1, 2, -1, 0])))
