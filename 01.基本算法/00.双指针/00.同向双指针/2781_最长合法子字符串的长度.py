class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fb = set(forbidden)
        left = 0
        ans = 0
        for right in range(len(word)):
            for i in range(right, right - 10, -1):
                if i < left:
                    break
                if word[i: right + 1] in fb:
                    left = i + 1
                    break
            ans = max(ans, right - left + 1)
        return ans