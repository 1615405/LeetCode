class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        pos = [0] * (len(grid) ** 2)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pos[x] = (i, j)
        
        if pos[0] != (0, 0):
            return False
        
        for (i, j), (x, y) in pairwise(pos):
            dx = abs(x - i)
            dy = abs(y - j)
            if dx * dy != 2:
                return False
        
        return True