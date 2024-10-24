"""Module providing class List"""
from typing import List

class Solution:
    """class docstring"""
    def remove_anagrams(self, words: List[str]) -> List[str]:

        """
        tc:O(n*m*log(m))
        sc:O(n*m)
        """
        former = ""
        ret_list = []
        for word in words:
            s_word = "".join(sorted(word))
            if s_word != former:
                ret_list.append(word)
                former = s_word
        return ret_list

a = Solution()
print(a.remove_anagrams(['ab','ba','c','e','d']))
