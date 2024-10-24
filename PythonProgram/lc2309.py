# import collections
class Solution:
    """Solution for lc2309"""
    def greatest_letter(self, s: str) -> str:
        """blank"""
        char_set = set([c for c in s])      
        ret = ''
        # print(charSet)
        for c in char_set:
            up = c.upper()
            lo = c.lower()
            if lo in char_set and up in char_set:
                ret = ret if ret and ret>up else up
        return ret
        # tc:O(N)
        # sc:O(1)




        # hashMap = collections.defaultdict(int)
        # charSet = set()
        # for c in s:
        #     hashMap[c]+=1
        #     charSet.add(c)
        
        # ret = ''
        # print(charSet)
        # for c in charSet:
        #     print(c)
        #     if c == c.lower() and c.upper() in charSet:
        #         if ret =='':
        #             ret == c.upper()
        #         else:
        #             ret == c.upper() if c.upper()>ret else ret
        #     elif c == c.upper() and c.lower() in charSet:
        #         if ret =='':
        #             ret == c
        #         else:
        #             ret == c if c > ret else ret
        #     print('ret = ',ret)

        # return ret
a = Solution()
print(a.greatest_letter('lEeTcOdE'))
