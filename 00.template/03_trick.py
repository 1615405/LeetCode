def isVowel(c: str) -> bool:
    # 判断字符 c 是否为 "aeiouAEIOU"
    c = ord(c) & 31
    return ((2130466 >> c) & 1) > 0