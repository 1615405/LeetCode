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




class Solution {
public:
    int balancedString(string s) {
        int n = s.length(), m = n / 4, cnt['X']{}; // 也可以用哈希表，不过数组更快一些
        for (char c : s) {
            ++cnt[c];
        }
        if (cnt['Q'] == m && cnt['W'] == m && cnt['E'] == m && cnt['R'] == m) {
            return 0;
        }
        int ans = n, left = 0;
        for (int right = 0; right < n; right++) { // 枚举子串右端点
            --cnt[s[right]];
            while (cnt['Q'] <= m && cnt['W'] <= m && cnt['E'] <= m && cnt['R'] <= m && left <= right) {
                ans = min(ans, right - left + 1);
                ++cnt[s[left++]]; // 缩小子串
            }
        }
        return ans;
    }
};