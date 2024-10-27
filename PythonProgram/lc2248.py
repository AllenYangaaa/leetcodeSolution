import collections
from typing import List


class Solution:
    '''class docstring'''
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """
        tc:O(n*m)
        sc:O(n*m)
        """
        ret = []
        cnt = collections.defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                cnt[nums[i][j]] += 1
        for item in cnt:
            if cnt[item] == len(nums):
                ret.append(item)
        return sorted(ret)
