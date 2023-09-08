class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replaces = [(c, 1) for c in s]
        for i, src, tar in zip(indices, sources, targets):
            if s.startswith(src, i):
                replaces[i] = (tar, len(src))
        
        ans = []
        i = 0
        while i < len(s):
            ans.append(replaces[i][0])
            i += replaces[i][1]
        return ''.join(ans)