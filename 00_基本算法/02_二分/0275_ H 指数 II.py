class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        while left < right:
            pivot = (left + right) // 2
            if citations[pivot] >= n - pivot:
                right = pivot
            else:
                left = pivot + 1
        return n - left if citations[left] >= n - left else 0