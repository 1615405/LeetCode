class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set(jewels)
        return sum(s in jewelSet for s in stones)