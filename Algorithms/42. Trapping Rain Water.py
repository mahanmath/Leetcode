class Solution:
    def trap(self, height: List[int]) -> int:
        
        L = len(height)
        max_forward = [0 for _ in range(L+ 2)]
        max_backward = [0 for _ in range(L + 2)]
        
        for i in range(1, L + 1):
            max_forward[i] = max([max_forward[i - 1], height[i - 1]])
            max_backward[L + 1 - i] = max([max_backward[L + 2 - i], height[L - i]])
        
        #print(max_forward)
        #print(max_backward)
        return sum([min([max_forward[i], max_backward[i]]) - height[i - 1] for i in range(1, L + 1)])