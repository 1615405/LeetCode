class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        cnt = Counter(ranks)
        left = 0
        right = min(cnt) * cars * cars
        while left < right:
            pivot = (left + right) // 2
            count = 0
            for r, c in cnt.items():
                x = isqrt(pivot // r) * c
                count += x
            if count < cars:
                left = pivot + 1
            else:
                right = pivot
        return left