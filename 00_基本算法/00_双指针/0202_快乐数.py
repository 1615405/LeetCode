class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum
        
        fastRunner, slowRunner = get_next(n), n
        while fastRunner != slowRunner:
            fastRunner = get_next(get_next(fastRunner))
            slowRunner = get_next(slowRunner)
        return fastRunner == 1