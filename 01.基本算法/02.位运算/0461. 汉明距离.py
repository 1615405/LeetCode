class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        Brain Kernighan 算法
        记 f(x) 表示 x 和 x-1 进行与运算所得的结果, f(x) = x & (x - 1),
        那么 f(x) 恰为 x 删去其二进制表示中最右侧的 1 的结果
        '''
        while s:
            s &= s - 1
            ret += 1
        return ret



class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        for i in range(32):
            num1 = (x >> i) & 1
            num2 = (y >> i) & 1
            if num1 is not num2:
                ret += 1
        return ret