from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = float("-inf")
        for i in range(len(nums)):
            if abs(nums[i]) < abs(ans):
                ans = nums[i]
            elif abs(nums[i]) == abs(ans):
                ans = max(nums[i], ans)
        return ans
        '''
        tc:O(n)
        sc:O(1)
        '''
        