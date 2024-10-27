from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for i in range(len(words)):
            if self.is_prefix(words[i], s):
                ans += 1
        return ans
    def is_prefix(self, a, b):
        """function judging if a is prefix of b"""
        if len(b) < len(a):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
    '''
    tc:O(m*n)
    sc:O(1)
    '''

aa = Solution()
print (aa.countPrefixes(["a","b","c","ab","bc","abc"], "abc"))
          