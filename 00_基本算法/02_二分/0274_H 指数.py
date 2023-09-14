class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n + 1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        tot = 0
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)
        while left < right:
            pivot = (left + right + 1) // 2
            cnt = 0
            for citation in citations:
                if citation >= pivot:
                    cnt += 1
            if cnt >= pivot:
                left = pivot
            else:
                right = pivot - 1
        return left