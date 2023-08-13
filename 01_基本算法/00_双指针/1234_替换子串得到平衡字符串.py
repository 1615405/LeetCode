class Solution:
    def balancedString(self, s: str) -> int:
        cnt, m = Counter(s), len(s) // 4
        ans, left = len(s) + 1, 0
        if all(cnt[x] <= m for x in "QWER"):
            return 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while all(cnt[x] <= m for x in "QWER") and left <= right:
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return ans