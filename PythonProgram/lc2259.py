class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        """
        tc:O(n)
        sc:O(1)
        """
        p = -1
        for i, num in enumerate(number):
            if digit == num:
                if i + 1 < len(number) and number[i + 1] > number[i]:
                    return number[:i] + number[i + 1:]
                elif i + 1 == len(number):
                    return number[:-1]
                else:
                    p = i
        return number[:p] + number[p + 1:]
