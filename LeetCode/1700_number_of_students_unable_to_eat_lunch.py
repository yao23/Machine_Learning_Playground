class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=yOfZ80BcUXE
        
        beats 63.27%
        """
        q = deque(students)
        for s in sandwiches:
            if s in q:
                while q[0] != s:
                    x = q.popleft()
                    q.append(x)
                q.popleft()
            else:
                return len(q)
        return 0
