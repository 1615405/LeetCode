def isVowel(c: str) -> bool:
    # 判断字符 c 是否为 "aeiouAEIOU"
    c = ord(c) & 31
    return ((2130466 >> c) & 1) > 0

def addDigits(self, num: int) -> int:
    '''
    数根又称数字根, 是自然数的一种性质，每个自然数都有一个数根。对于给定的自然数，反复将各个位上的数字相加，
    直到结果为一位数，则该一位数即为原自然数的数根。
    '''
    return (num - 1) % 9 + 1 if num else 0