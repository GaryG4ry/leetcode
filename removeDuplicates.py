class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        # # with extra place
        # dic = {}
        # for i in range(length):
        #     if nums[i] not in dic:
        #         dic[nums[i]] = 1
        #     else:
        #         dic[nums[i]] += 1
        #
        # return len(dic)

        # with no extra place
        if length == 0:
            return 0
        i = 0
        for j in range(1, length):
            if nums[j] != nums[i]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
        return i+1




print(Solution().removeDuplicates([]))
