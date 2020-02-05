class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        L = len(nums)
        if(k >= L):
            k = L - 1
        sorted_k = nums[:k + 1]
        sorted_k.sort()
        def findinSorted(arr, val):
            if(not arr):
                return -1
            left = 0
            right = len(arr) - 1
            while(right >= left):
                mid = (right + left)//2
                #print(left, mid, right)
                if(arr[mid] < val):
                    left = mid + 1
                elif(arr[mid] == val):
                    return mid
                else:
                    right = mid - 1
            return right
        
        for j in range(k):
            if(abs(sorted_k[j + 1] - sorted_k[j]) <= t):
                return True
            
        for i in range(k + 1, L):
            #print(sorted_k)
            
            indx_old = findinSorted(sorted_k, nums[i - k - 1])    
            sorted_k.pop(indx_old)
            indx_new = findinSorted(sorted_k, nums[i])
            sorted_k.insert(indx_new + 1, nums[i])
            
            if(indx_new >= 0 and abs(sorted_k[indx_new + 1] - sorted_k[indx_new]) <= t):
                return True
            
            if(indx_new <= k - 2 and abs(sorted_k[indx_new + 1] - sorted_k[indx_new + 2]) <= t):
                return True
            
        return False
            
        
