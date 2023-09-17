class Solution:
    def isUnique(self, astr: str) -> bool:
        mask = 0
        for x in astr:
            move_bit = ord(x) - ord('a')
            if mask & (1 << move_bit):
                return False
            else:
                mask |= (1 << move_bit)
        return True