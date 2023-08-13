class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        cnt = Counter()
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1 and left <= right:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans