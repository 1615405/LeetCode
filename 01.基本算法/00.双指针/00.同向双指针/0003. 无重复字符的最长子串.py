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



class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hashtable;
        int left = 0, ans = 0;
        for (int right = 0; right < s.size(); right++) {
            hashtable[s[right]]++;
            while (hashtable[s[right]] > 1 && left <= right) {
                hashtable[s[left]]--;
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};