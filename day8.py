#move zeros solution
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 'j' is the index where the next non-zero element should go
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # place nums[i] at nums[j] (may be same index)
                nums[j] = nums[i]
                j += 1
        # fill remaining positions with zeros
        for k in range(j, len(nums)):
            nums[k] = 0
