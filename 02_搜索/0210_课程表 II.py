class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adjaceny = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            adjaceny[pre].append(cur)
            indegrees[cur] += 1
        
        queue = deque()
        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
        
        ans = []
        while queue:
            pre = queue.popleft()
            ans.append(pre)
            numCourses -= 1
            for cur in adjaceny[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        
        if not numCourses:
            return ans
        else:
            return []