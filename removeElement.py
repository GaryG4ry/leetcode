class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return
        # j = length-1
        # for i in range(length):
        #     if nums[i] == val:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        #     if i == j:
        #         break
        # return nums
        j = 0
        for i in range(length):
            if nums[i] != val:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return j


print(Solution().removeElement([3,2,2,3], 3))
