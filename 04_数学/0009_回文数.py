class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        if x > 0 and x % 10 == 0:
            return False
        if x == 0:
            return True
        while x > ans:
            ans = ans * 10 + x % 10
            x //= 10
        return ans // 10 == x or ans == x