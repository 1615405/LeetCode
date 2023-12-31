class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        python 对有符号整数类型和无符号整数类型没有区分。有符号整数类型的
        第31个二进制位(即最高位)是补码意义下的符号位，对应着-2^31
        '''
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            if count % 3 != 0:
                if i == 31:
                    print(1 << i)  # c++中输出为 -2147483648, 编译器解释为负数
                    result -= 1 << i
                else:
                    result += 1 << i
        return result