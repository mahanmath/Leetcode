class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if(len(nums) < 3):
            return []
        
        output = []
        nums.sort()
        nums_neg = []
        nums_pos = []
        zero_count = 0
        for i in range(len(nums)):
            if(nums[i] < 0):
                if(i < 2 or nums[i] != nums[i - 2]):
                    nums_neg.append(nums[i])
            elif(i < 2 or nums[i] != nums[i - 2]):
                nums_pos.append(nums[i])
                
            zero_count += int(nums[i] == 0)
            
        if(zero_count >= 3):
            output.append([0,0,0])
        if(zero_count == 0):
            zero_exist = False
        else:
            zero_exist = True

        #Two positive and one negative
        for neg in set(nums_neg):
            target = -1 * neg
            left = 0
            right = len(nums_pos) - 1
            while(left < right):
                #print(neg, left, right, output)
                SUM = nums_pos[left] + nums_pos[right]
                if(SUM < target):
                    left += 1
                elif(SUM > target):
                    right -= 1
                elif(not output or output[-1][-1] != neg or output[-1][0] != nums_pos[left]):
                    output.append([nums_pos[left], nums_pos[right], neg])
                    left += 1
                    right -= 1
                else:
                    left += 1

        #Two negative and one positive
        for target in set(nums_pos):
            left = 0
            right = len(nums_neg) - 1
            while(left < right):
                SUM = -1*(nums_neg[left] + nums_neg[right])
                if(SUM < target):
                    right -= 1
                elif(SUM > target):
                    left += 1
                elif(not output or output[-1][-1] != target or output[-1][0] != nums_neg[left]):
                    output.append([nums_neg[left], nums_neg[right], target]) 
                    left += 1
                    right -= 1
                else:
                    left += 1
        return output
                    
            
        
