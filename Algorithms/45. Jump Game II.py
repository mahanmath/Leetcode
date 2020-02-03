class Solution:
    def jump(self, nums: List[int]) -> bool:
        L = len(nums)
        if(L == 1):
            return(0)
        max_from_left = [0 for _ in range(L)]
        max_from_left[0] = min([L - 1, nums[0]])
        
        for i in range(1, L):
            max_from_left[i] = max([max_from_left[i - 1], i + nums[i]])
            max_from_left[i] = min([L - 1, max_from_left[i]])
        
        ans = 0
        indx = 0
        while(indx != L - 1):
            indx = max_from_left[indx]
            ans += 1
        return ans