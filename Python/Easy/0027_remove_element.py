class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for items in range(len(nums)):
            if nums[items] != val:
                nums[index] = nums[items]
                index += 1
        return index
if __name__ == "__main__":
    assert Solution().removeElement([3, 2, 2, 3], 3) == 2
    assert Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5