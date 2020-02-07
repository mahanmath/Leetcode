class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        length = len(A)
        output = len(A) + 1
        
        # Partial sums
        S = [0]
        for num in A:
            S.append(S[-1] + num)
        
        from collections import deque
        
        Q = deque()
        
        for indx, S_indx in enumerate(S):
            
            while(Q and S[Q[-1]] >= S_indx):
                Q.pop()
            
            while(Q and S_indx - S[Q[0]] >= K):
                output = min([output, indx - Q[0]])
                Q.popleft()
                
            Q.append(indx)
        
        return output if output < length+1 else -1
                
