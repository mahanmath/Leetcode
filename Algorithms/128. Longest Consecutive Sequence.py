class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) < 2):
            return len(nums)
        #Hash = {num: [False, max_from_here]}
        MyHash = {}
        
        for num in nums:
            if(not num in MyHash):
                MyHash[num] = [False, 1]
        self.ans = 0
        def MaxPathFromHere(self, num):
            if(MyHash[num][0]):
                return MyHash[num][1]
            else:
                MyHash[num][0] = True
                if(num+1 in MyHash):
                    MyHash[num][1] = 1 + MaxPathFromHere(self, num + 1)
                else:
                    MyHash[num][1] = 1
                self.ans = max([self.ans, MyHash[num][1]])
                return MyHash[num][1]
        for num in MyHash:
            MaxPathFromHere(self, num)
        
        return self.ans