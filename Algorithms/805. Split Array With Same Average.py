class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        
        import numpy as np
        
        L = len(A)
        
        if(L == 1): return False
        
        A = list(map(lambda x: x*L, A))
        M = sum(A)//L
        A = list(map(lambda x: x - M, A))
        
        A_1 = np.array(A[: L//2])
        A_2 = np.array(A[L//2:])
        L_2 = len(A_2)
        subsetSum = set()
        
        for i in range(1, 2 ** (L//2)):
            s = bin(i)
            subVec = np.array([0 for _ in range(L//2 - len(s) + 2)] + [int(char) for char in s[2:]])
            subsetSum.add(A_1.dot(subVec))
            
            
        if 0 in subsetSum: return True
        
        
        for i in range(1, 2 ** (L_2) - 1):
            s = bin(i)
            subVec = np.array([0 for _ in range(L_2 - len(s) + 2)] + [int(char) for char in s[2:]])
            if (-1* A_2.dot(subVec)) in subsetSum:
                return True
        
        subsetSum.remove(A_1.sum())
        
        if (-1* A_2.sum()) in subsetSum:
            return True
        
        return False
        
        