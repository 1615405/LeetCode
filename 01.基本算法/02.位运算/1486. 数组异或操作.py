'''
1. 异或的性质
    x ^ x = 0
    x ^ y = y ^ x
    (x ^ y) ^ z = x ^ (y ^ z)
    x ^ y ^ y = x
    对于任意整数 i, 有
        4i ^ (4i + 1) ^ (4i + 2) ^ (4i + 3) = 0

2.  sumXor(x), 计算 0 ^ 1 ^ 2 ^ ⋯ ^ X
    当 x = 4k:     sumXor(x) = x
    当 x = 4k + 1: sumXor(x) = (x - 1) XOR x
    当 x = 4k + 2: sumXor(x) = (x - 2) XOR (x - 1) XOR x
    当 x = 4k + 3: sumXor(x) = (x - 3) XOR (x - 2) XOR (x - 1) XOR x
    进一步化简为
        x = 4k     => sumXor(x) = x
        x = 4k + 1 => sumXor(x) = 1
        x = 4k + 2 => sumXor(x) = x + 1
        x = 4k + 3 => sumXor(x) = 0

3. start ^ (start + 2i) ^ (start + 4i) ^ ⋯ ^ (start + 2(n - 1))
    这些数的奇偶性质相同，可以把参与运算的数的二进制位的最低位提取出来单独处理。 
    整体右移一位，新式 = s ^ (s + 1) ^ (s + 2) ^ ⋯ ^ (s + n - 1), 其中
    s = start // 2(下取整)

4. 假设我们最终的答案为 ans. 整个处理过程其实就是把原式中的每个 s 右移一位, 然后再将 ans 进行一位左移,
将原本丢失的最后一位结果重新补上。
'''

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        def sumXor(x: int) -> int:
            if x % 4 == 0:
                return x
            elif x % 4 == 1:
                return 1
            elif x % 4 == 2:
                return x + 1
            return 0
        s = start >> 1
        e = n & start & 1
        ret = sumXor(s - 1) ^ sumXor(s + n - 1)
        return ret << 1 | e