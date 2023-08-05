def hammingWeight(self, n: int) -> int:
    def lowbit(x: int) -> int:
        return x & (-x)
    ret = 0
    while n > 0:
        ret += 1
        n -= lowbit(n)
    return ret


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


def hammingWeight(self, n: int) -> int:
    n = (n & 0x55555555) + ((n >> 1)  & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2)  & 0x33333333)
    n = (n & 0x0f0f0f0f) + ((n >> 4)  & 0x0f0f0f0f)
    n = (n & 0x00ff00ff) + ((n >> 8)  & 0x00ff00ff)
    n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
    return n


def sumXor(x: int) -> int:
    '''
    sumXor(x), 计算 0 ^ 1 ^ 2 ^ ⋯ ^ x
        当 x = 4k:     sumXor(x) = x
        当 x = 4k + 1: sumXor(x) = (x - 1) XOR x
        当 x = 4k + 2: sumXor(x) = (x - 2) XOR (x - 1) XOR x
        当 x = 4k + 3: sumXor(x) = (x - 3) XOR (x - 2) XOR (x - 1) XOR x
        进一步化简为
            x = 4k     => sumXor(x) = x
            x = 4k + 1 => sumXor(x) = 1
            x = 4k + 2 => sumXor(x) = x + 1
            x = 4k + 3 => sumXor(x) = 0
    '''
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x + 1
    return 0