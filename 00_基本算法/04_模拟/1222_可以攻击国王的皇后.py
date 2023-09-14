class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        s = set(map(tuple, queens))
        ans = []

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                x, y = king[0] + dx, king[1] + dy
                while 0 <= x <= 8 and 0 <= y <= 8:
                    if (x, y) in s:
                        ans.append([x, y])
                        break
                    x += dx
                    y += dy
        
        return ans