class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        for i in range(32):
            num1 = (x >> i) & 1
            num2 = (y >> i) & 1
            if num1 is not num2:
                ret += 1
        return ret