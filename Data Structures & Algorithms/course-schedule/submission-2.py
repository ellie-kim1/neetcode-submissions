class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
       
        indegree = {}
        pre_req = {}
       
        for i in range(numCourses):
            indegree[i] = 0
            pre_req[i] = []
    
        for a, b in prerequisites:
            indegree[a] += 1
            pre_req[b].append(a)
        
        queue = deque([node for node in indegree if indegree[node]== 0])

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for next_course in pre_req[node]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return len(order) == numCourses

# Time: O(V+E) -- visit every reachable node and examine their edges
# Space: O(V+E) -- store all vertices and their edges