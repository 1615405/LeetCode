class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        for i in range(0, 32):
            ret += ((n >> i) & 1)
        return ret



class Solution:
    def hammingWeight(self, n: int) -> int:
        def lowbit(x: int) -> int:
            return x & (-x)
        ret = 0
        while n > 0:
            ret += 1
            n -= lowbit(n)
        return ret




class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Brain Kernighan 算法
        记 f(x) 表示 x 和 x-1 进行与运算所得的结果, f(x) = x & (x - 1),
        那么 f(x) 恰为 x 删去其二进制表示中最右侧的 1 的结果
        '''
        ret = 0
        while n > 0:
            ret += 1
            n = n & (n - 1)
        return ret



class Solution:
    def hammingWeight(self, n: int) -> int:
        n = (n & 0x55555555) + ((n >> 1)  & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2)  & 0x33333333)
        n = (n & 0x0f0f0f0f) + ((n >> 4)  & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + ((n >> 8)  & 0x00ff00ff)
        n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
        return n