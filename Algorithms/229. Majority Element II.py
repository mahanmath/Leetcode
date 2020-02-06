class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ans = []
		
        else:
            candid1, candid2, count1, count2 = -1, -1, 0, 0
            
        for num in nums: 
        
            if num == candid1: 
                count1 += 1
            elif num == candid2: 
                count2 += 1
            elif count1 == 0: 
                candid1, count1 = num, 1
            elif count2 == 0: 
                candid2, count2 = num, 1
            else:
                count1, count2 = count1-1, count2-1
        
        if (count1 > 0) and (nums.count(candid1) > len(nums)//3): 
            ans.append(candid1)
            
        if (count2 > 0) and (nums.count(candid2) > len(nums)//3): 
            ans.append(candid2)
    
        return ans
