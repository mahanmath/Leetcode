class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def DIST(p, q):
            return ((p[0] - q[0])**2 + (p[1] - q[1])**2)
        
        distances = [DIST(p1, p2),
                     DIST(p1, p3),
                     DIST(p1, p4),
                     DIST(p2, p3),
                     DIST(p2, p4),
                     DIST(p3, p4)]
        distances.sort()
        m = distances[0]
        if(m == 0): return False
        return(distances == [m, m, m, m, 2*m, 2*m])