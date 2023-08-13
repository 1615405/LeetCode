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


class Solution:
    # 牛顿迭代法
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        
        return int(x0)