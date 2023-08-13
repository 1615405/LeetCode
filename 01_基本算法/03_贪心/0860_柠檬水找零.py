class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for _, x in enumerate(bills):
            if x == 5:
                five += 1
            elif x == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            else:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True