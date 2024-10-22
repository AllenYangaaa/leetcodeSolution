from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        former = ""
        retList = []
        for word in words:
            sWord = "".join(sorted(word))
            if sWord != former:
                retList.append(word)
                former = sWord
        return retList

        """
        tc:O(n*m*log(m))
        sc：O(n*m)
        """

    
a = Solution()
print(a.removeAnagrams(['ab','ba','c','e','d']))