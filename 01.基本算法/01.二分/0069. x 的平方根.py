class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            pivot = (left + right + 1) // 2
            if pivot * pivot > x:
                right = pivot - 1
            else:
                left = pivot
        return left