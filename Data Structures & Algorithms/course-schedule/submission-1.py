class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        input:
        numCourses = 3
        prerequisites = [[0, 1]]

        ---------------------------
        courses: [0, 1, 2]

        indegree = {
            0: 1
            1: 0
            2: 0
        }

        queue = [1, 2]

        ---------------------------

        order = []

        '''

        indegree = {}
        prereq = {}

        for i in range(numCourses):
            indegree[i] = 0
            prereq[i] = []
        
        # indegree = {
        #   0 : 0
        #   1 : 0
        #   2 : 0
        #}

        # prereq = {
        #   0 : []
        #   1 : []
        #   2 : []
        #}
        
        for a, b in prerequisites:
            indegree[a] += 1 # course a requires +1 prerequisite
            prereq[b].append(a) # completing course b unlocks course a
        
        # indegree = {
        #   0 : 1
        #   1 : 0
        #   2 : 0
        #}

        # prereq = {
        #   0 : []
        #   1 : [0]
        #   2 : []
        #}

        queue = deque([course for course in indegree if indegree[course] == 0])

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for associated_course in prereq[course]:
                indegree[associated_course] -= 1

                if indegree[associated_course] == 0:
                    queue.append(associated_course)
        
        return len(order) == numCourses

# Time: O(V+E) -- visit every reachable course and examnine its neighboring courses
# Space: O(V) -- adjacency list stores both the vertices and edges