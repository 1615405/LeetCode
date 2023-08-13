class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dfs(r: int, c: int) -> int:
            if c < 0 or c >= n:
                return inf
            if r == 0:
                return matrix[0][c]
            return min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]
        return min(dfs(n - 1, i) for i in range(n))



class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [matrix[0]]
        n = len(matrix)
        for i in range(1, n):
            cur = [0] * n
            for j in range(n):
                mn = dp[-1][j]
                if j > 0:
                    mn = min(mn, dp[-1][j - 1])
                if j < n - 1:
                    mn = min(mn, dp[-1][j + 1])
                cur[j] = mn + matrix[i][j]
            dp.append(cur)
        return min(dp[-1])