class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low: int, high: int) -> bool:
            while low < high:
                if s[low] == s[high]:
                    low += 1
                    high -= 1
                else:
                    return False
            return True

        n = len(s)
        left, right = 0, n - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)
        return True