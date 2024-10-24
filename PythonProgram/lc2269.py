class Solution:
    "Class docstring"
    def divisor_substrings(self, num: int, k: int) -> int:
        '''
            tc:O(n)
            sc:O(1)
        '''
        ret = 0
        num_str = str(num)
        for i in range(len(num_str) - k + 1):
            wd = int(num_str[i: i + k])
            if wd != 0 and num % a == 0:
                ret += 1
        return ret

a = Solution()
print(a.divisor_substrings(240,2))

print(a.divisor_substrings(430043,2))
